import base64
from typing import List
import time
import os
import zipfile
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.conf import settings
from data.models import Supplier


class GmailException(Exception):
    """gmail base exception class"""


class NoEmailFound(GmailException):

    """no email found"""


def search_emails(service, query_string: str, label_ids: List = None):

    """Some code here"""

    try:
        message_list_responce = (
            service.users()
            .messages()
            .list(userId="me", labelIds=label_ids, q=query_string)
            .execute()
        )
        return message_list_responce

    except Exception as e:
        raise NoEmailFound("No emails returned")


def get_file_data(service, message_id, attachment_id, file_name, save_location):
    """Functin for getting and saving attachments"""
    response = (
        service.users()
        .messages()
        .attachments()
        .get(userId="me", messageId=message_id, id=attachment_id)
        .execute()
    )
    file_data = base64.urlsafe_b64decode(response.get("data").encode("UTF-8"))
    return file_data


def get_message_details(
    service, message_id, msg_format="metadata", metadata_headers: List = None
):
    """Getting data from messages"""
    message_details = (
        service.users()
        .messages()
        .get(
            userId="me",
            id=message_id,
            format=msg_format,
            metadataHeaders=metadata_headers,
        )
        .execute()
    )
    return message_details


def delete_message(service, message_id):
    """Deleting message after getting content"""
    delete = service.users().messages().delete(userId="me", id=message_id).execute()


SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]


def check_emails_and_save_attachments(email_address: str, supplier_name: str):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    date = []
    credentials_path = os.path.join(settings.BASE_DIR, "data/credentials.json")
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)

        q = f"is:unread from:{email_address} has:attachment"

        # needs to be refactored to one place
        save_location = os.path.join(settings.BASE_DIR, "tmp/input")

        emails = search_emails(service, q)
        if "messages" in emails:
            for email in emails["messages"]:
                message_details = get_message_details(
                    service, email["id"], msg_format="full", metadata_headers=["parts"]
                )
                messageDetailPayload = message_details.get("payload")
                date = filter(
                    lambda header: header["name"] == "Date",
                    messageDetailPayload["headers"],
                )

                if "parts" in messageDetailPayload:
                    for msgPayload in messageDetailPayload["parts"]:
                        filename, file_ext = os.path.splitext(msgPayload["filename"])

                        file_name = msgPayload["filename"]
                        dir_name = os.path.join(save_location, supplier_name)

                        """Here remove files goes"""
                        try:
                            del_files = os.listdir(dir_name)
                            for name in del_files:
                                d_f = os.path.join(dir_name, name)
                                os.remove(d_f)
                        except:
                            print("No files or dirs to rmove")
                            """Until here"""
                        if not os.path.exists(dir_name):
                            os.makedirs(dir_name)

                        body = msgPayload["body"]
                        if "attachmentId" in body:
                            attachment_id = body["attachmentId"]
                            attachment_content = get_file_data(
                                service,
                                email["id"],
                                attachment_id,
                                file_name,
                                save_location,
                            )
                            with open(os.path.join(dir_name, file_name), "wb") as f:
                                try:
                                    f.write(attachment_content)
                                    print(f"File {file_name} saved to {dir_name}")
                                    service.users().messages().modify(
                                        userId="me",
                                        id=email["id"],
                                        body={
                                            "removeLabelIds": ["UNREAD"],
                                            "addLabelIds": [],
                                        },
                                    ).execute()
                                except Exception as e:
                                    print("File has not being saved", e)

                time.sleep(0.5)
        else:
            print("No messages found")

    except HttpError as error:
        # (developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")

    return list(date)
