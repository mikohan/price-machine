from data.views import current_datetime, get_emails
from django.urls import path

urlpatterns = [
    path("", current_datetime, name="test-home"),
    path("emails/", get_emails, name="get-emails"),
]
