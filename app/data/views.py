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
import openpyxl as xl
import time

path_to_get = os.path.join(settings.BASE_DIR, "tmp/input")
path_to_save = os.path.join(settings.BASE_DIR, "tmp/csv")


def unzip_all_suppliers(supplier):
    """Check if some files saved in zip"""
    working_dir = os.path.join(settings.BASE_DIR, path_to_get, supplier.name.lower())
    p = Path(working_dir)
    print(list(p.glob("**/*.zip")))
    for item in list(p.glob("**/*.zip")):
        print(item.parent)
        with zipfile.ZipFile(item, "r") as zip_f:
            zip_f.extractall(item.parents[0])


def update_date(supplier, str_date):

    """Updated date if price was received"""
    date_time = parser.parse(str_date)
    supplier.updated_price = date_time
    supplier.save()
    return supplier.updated_price


def get_emails(request):
    """Getting emails with attachments and save it in folder"""

    suppliers = Supplier.objects.all()
    dates = []
    for supplier in suppliers:
        try:
            res = check_emails_and_save_attachments(supplier.email, supplier.name)
            update_date(supplier, res)

            dates.append({"Date": res})
            print(res)
        except Exception as e:
            print("Emails not received")

    html = f"<html><body>Some stuff{json.dumps(dates)}</body></html>"
    return HttpResponse(html)


def col_count(path):
    ext = Path(path).suffix
    if ".xlsx" == ext:
        try:
            wb = xl.load_workbook(path, enumerate)
            sheet = wb.worksheets[0]
            column_count = sheet.max_column
            return column_count
        except Exception as e:
            print("Something wrong in co_count function", e)
            return False
    return False


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
        raw_cols = json.loads(supplier.price_fields)
        len_raw_cols = len(raw_cols)
        col_cnt = col_count(src)
        if col_cnt > len_raw_cols:
            dif = col_cnt - len_raw_cols
            for n in range(dif):
                raw_cols.append("emp")
        try:
            try:
                df = pd.DataFrame(
                    pd.read_excel(
                        src,
                        names=raw_cols,
                        header=0,
                        skiprows=range(1, skip_rows),
                    )
                )
            except:
                df = pd.DataFrame(
                    pd.read_excel(
                        src,
                        names=raw_cols,
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


def get_supplier(request, pk):
    """
    Workflow for getting prices for specific supplier
    """
    supplier = Supplier.objects.get(pk=pk)

    res = check_emails_and_save_attachments(supplier.email, supplier.name)
    if res:
        unzip_all_suppliers(supplier)
        transform_excel(supplier)
        upd_date = update_date(supplier, res)
        print("Price date has been updated!", str(upd_date))

    return HttpResponse(f"<h1>{json.dumps(res)}</h1>")


def get_suppliers(request):
    """Workflow of getting prices for all suppliers"""
    start_time = time.time()
    suppliers = Supplier.objects.filter(enabled=True)
    updated_prices = []
    # for supplier in suppliers:
    #     res = check_emails_and_save_attachments(supplier.email, supplier.name)
    #     if res:
    #         unzip_all_suppliers(supplier)
    #         transform_excel(supplier)
    #         upd_date = update_date(supplier, res)
    #         upd = str(upd_date)
    #         updated_prices.append({supplier.name: upd})
    #     else:
    #         updated_prices.append({supplier.name: "Not Updated"})
    # work_time = int(time.time() - start_time)
    # updated_prices.append({"Script worked seconds:": work_time})
    context = {"Var": "Hello world"}

    return render(request, "suppliers.html", context)

    # return HttpResponse(f"<h4>{json.dumps(updated_prices)}</h4>")


def list_suppliers(request):
    """Listing suppliers"""
    suppliers = Supplier.objects.filter(enabled=True).order_by("-weight")
    context = {"suppliers": suppliers}

    return render(request, "suppliers_list.html", context)


def home(request):
    unzip_all_suppliers()
    return HttpResponse("<h1>Some stuff</h1>")
