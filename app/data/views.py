from tabnanny import check
from django.shortcuts import render
from django.http import HttpResponse
import datetime, os, json
import pandas as pd
from django.conf import settings, settings
from .models import Supplier
import glob
from data.get_email_attachments import check_emails_and_save_attachments

path = os.path.join(settings.BASE_DIR, "shared_data/motordjidiler2.xls")


def get_emails(request):
    """Getting emails with attachments and save it in folder"""

    response = check_emails_and_save_attachments()
    html = f"<html><body>Some stuff{response}</body></html>"
    return HttpResponse(html)


def current_datetime(request):

    suppliers = Supplier.objects.filter(enabled=True)
    path_to_get = os.path.join(settings.BASE_DIR, "shared_data/input")
    path_to_save = os.path.join(settings.BASE_DIR, "shared_data/csv")
    cols_ready = ["name", "brand", "cat", "cat2", "price", "stock"]
    done = []
    for supplier in suppliers:
        price_fields = json.loads(supplier.price_fields)
        skip_rows = 1
        if supplier.skip_rows:
            skip_rows = supplier.skip_rows
        file_src = glob.glob(os.path.join(path_to_get, supplier.name.lower() + ".*"))[0]
        df = pd.DataFrame(
            pd.read_excel(
                file_src, names=price_fields, header=0, skiprows=range(1, skip_rows)
            )
        )
        if "cat2" not in df.columns:
            df["cat2"] = ""
        df_reorder = df[cols_ready]
        df_reorder.to_csv(
            os.path.join(path_to_save, supplier.name.lower() + ".csv"),
            index=False,
            sep=";",
            encoding="utf-8",
        )
        done.append({supplier.name: len(df.index)})
    print_res = json.dumps(done)

    html = f"<html><body><div>Saved {print_res} rows.</div><div> Some text  </div></body></html>"
    return HttpResponse(html)


# Create your views here.
