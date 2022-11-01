import parser
from tabnanny import check
from django.shortcuts import render
from django.http import HttpResponse
import os, json
from datetime import datetime
import pandas as pd
from django.conf import settings, settings
from .models import Supplier
import glob
from pathlib import Path
import zipfile
from dateutil import parser
from data.get_email_attachments import check_emails_and_save_attachments

path_to_get = os.path.join(settings.BASE_DIR, "tmp/input")
path_to_save = os.path.join(settings.BASE_DIR, "tmp/csv")


def unzip_all_suppliers():
    """Check if some files saved in zip"""
    working_dir = os.path.join(settings.BASE_DIR, path_to_get)
    p = Path(working_dir)
    print(list(p.glob("**/*.zip")))
    for item in list(p.glob("**/*.zip")):
        print(item.parent)
        with zipfile.ZipFile(item, "r") as zip_f:
            zip_f.extractall(item.parents[0])


def get_emails(request):
    """Getting emails with attachments and save it in folder"""

    suppliers = Supplier.objects.all()
    dates = []
    for supplier in suppliers:
        res = check_emails_and_save_attachments(supplier.email, supplier.name)
        str_date = res[0]["value"]
        date_time = parser.parse(str_date)
        supplier.updated_price = date_time
        supplier.save()

        dates.append(res)
        print(res)

    response = check_emails_and_save_attachments("price@rossko.ru", "rossko")
    dates = []
    html = f"<html><body>Some stuff{json.dumps(dates)}</body></html>"
    return HttpResponse(html)


def transform_excel(supplier):
    """Function iterate suppliers,
    transform files into right csv format,
    and save it into csv dir"""
    cols_ready = [
        "name",
        "brand",
        "cat",
        "cat2",
        "price",
        "stock",
        "supplier_name",
        "supplier_item_id",
        "car",
    ]
    skip_rows = 1
    if supplier.skip_rows:
        skip_rows = supplier.skip_rows
    supplier_dir = Path(os.path.join(path_to_get, supplier.name.lower()))
    files_src = supplier_dir.glob("*.[xl]*")
    ret = []

    for i, src in enumerate(files_src):
        try:
            try:
                df = pd.DataFrame(
                    pd.read_excel(
                        src,
                        names=json.loads(supplier.price_fields),
                        header=0,
                        skiprows=range(1, skip_rows),
                    )
                )
            except:
                df = pd.DataFrame(
                    pd.read_excel(
                        src,
                        names=json.loads(supplier.price_fields),
                        skiprows=range(1, skip_rows),
                        header=0,
                        engine="odf",
                    )
                )

            if "cat2" not in df.columns:
                df["cat2"] = ""
            if "supplier_name" not in df.columns:
                df["supplier_name"] = supplier.name
            if "car" not in df.columns:
                df["car"] = ""
            if "supplier_item_id" not in df.columns:
                df["supplier_item_id"] = ""
            df_reorder = df[cols_ready]
            saved_path = os.path.join(
                path_to_save, supplier.name.lower() + "_" + str(i) + ".csv"
            )
            df_reorder.to_csv(
                saved_path,
                index=False,
                sep=";",
                encoding="utf-8",
            )

            ret.append(saved_path)
        except Exception as e:
            print(supplier.name, e)

    return ret


def transform_prices(request):

    ret = []
    suppliers = Supplier.objects.filter(enabled=True)
    for supplier in suppliers:
        ret.append(transform_excel(supplier))

    html = (
        f"<html><body><div>{json.dumps(ret)}</div><div> Some text  </div></body></html>"
    )
    return HttpResponse(html)


# Create your views here.


def home(request):
    unzip_all_suppliers()
    return HttpResponse("<h1>Some stuff</h1>")
