import parser
from tabnanny import check
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os, json
from datetime import datetime
import pandas as pd
from django.conf import settings
from .models import Supplier
import glob
from pathlib import Path
import zipfile
from dateutil import parser
from data.get_email_attachments import check_emails_and_save_attachments
import openpyxl as xl
import time
import hashlib
from data.lib.one_c_fixer import fix_truck_motors
import requests
from requests.auth import HTTPBasicAuth
import re
from http import HTTPStatus

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


def strip_whitespace(text):
    """Functon removes whitespases in names befor inserting in pandas"""
    try:
        return text.strip()
    except AttributeError:
        return text


def make_uuid(name, brand):
    """Make unique ID from Name and brand"""
    string = str(name) + str(brand)
    m = hashlib.md5()
    m.update(string.encode("utf-8"))
    return str(int(m.hexdigest(), 16))[0:12]


def transform_excel(supplier):
    """Function iterate suppliers,
    transform files into right csv format,
    and save it into csv dir"""
    cols_ready = [
        "uuid",
        "name",
        "brand",
        "cat",
        "cat2",
        "price",
        "stock",
        "supplier_name",
        "supplier_item_id",
        "car",
        "updated",
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

        # fixing truck motors file
        if supplier.name == "trackmotors":
            fix_truck_motors(src)

        if col_cnt > len_raw_cols:
            dif = col_cnt - len_raw_cols
            for n in range(dif):
                raw_cols.append("emp")
        try:
            # try:

            df = pd.DataFrame(
                pd.read_excel(
                    src,
                    names=raw_cols,
                    header=0,
                    skiprows=range(1, skip_rows),
                    converters={
                        "name": strip_whitespace,
                        "cat": strip_whitespace,
                    },
                )
            )
            # except Exception as e:
            #     df = pd.DataFrame(
            #         pd.read_excel(
            #             src,
            #             names=raw_cols,
            #             skiprows=range(1, skip_rows),
            #             header=0,
            #             engine="odf",
            #             converters={
            #                 "name": strip_whitespace,
            #                 "cat": strip_whitespace,
            #             },
            #         )
            #     )
            #     print("In first exception where engine is odf", e)
            df = df.dropna(subset=["name", "cat"])
            df["uuid"] = df.apply(
                lambda x: make_uuid(name=x["price"], brand=x["brand"]), axis=1
            )

            if "cat2" not in df.columns:
                df["cat2"] = ""
            if "supplier_name" not in df.columns:
                df["supplier_name"] = supplier.name
            if "car" not in df.columns:
                df["car"] = ""
            if "supplier_item_id" not in df.columns:
                df["supplier_item_id"] = ""
            if "updated" not in df.columns:
                df["updated"] = supplier.updated_price
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
    suppliers = Supplier.objects.get(id=8)
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

    # transform_excel(supplier)
    res = check_emails_and_save_attachments(supplier.email, supplier.name)
    if res:
        unzip_all_suppliers(supplier)
        transform_excel(supplier)
        upd_date = update_date(supplier, res)
        print("Price date has been updated!", str(upd_date))
    return JsonResponse({"all": "good"})

    # return HttpResponse(f"<h1>{json.dumps(res)}</h1>")


from django.core import serializers


def get_suppliers(request):
    """Workflow of getting prices for all suppliers"""
    start_time = time.time()
    suppliers = Supplier.objects.filter(enabled=True)
    updated_prices = []
    for supplier in suppliers:
        res = check_emails_and_save_attachments(supplier.email, supplier.name)
        if res:
            unzip_all_suppliers(supplier)
            transform_excel(supplier)
            upd_date = update_date(supplier, res)
            upd = str(upd_date.replace(tzinfo=None))
            updated_prices.append({supplier.show_name: f"{upd}"})
        else:
            updated_prices.append({supplier.show_name: False})
    work_time = int(time.time() - start_time)

    return JsonResponse({"foo": updated_prices, "time": work_time})

    # return HttpResponse(f"<h4>{json.dumps(updated_prices)}</h4>")


def list_suppliers(request):
    """Listing suppliers"""
    suppliers = Supplier.objects.filter(enabled=True).order_by("-weight")
    supplier = suppliers.first()
    context = {"suppliers": suppliers, "PRICE_EXPERATION": settings.PRICE_EXPERATION}

    return render(request, "suppliers_list.html", context)


def experiment(request):
    """Used for experiments with some stuff"""

    start_time = time.time()
    sups = Supplier.objects.all()

    for sup in sups:
        transform_excel(sup)

    context = {"time": round(time.time() - start_time)}
    return HttpResponse(json.dumps(context))


def ajax_upate_supplier(request):
    time.sleep(4)
    return JsonResponse({"foo": "bar"})


def home(request):
    """Function for mani page with searches"""
    context = {
        "FRONT_SEARCH_URL": settings.FRONT_SEARCH_URL,
        "FRONT_SEARCH_URL_ANGARA": settings.FRONT_SEARCH_URL_ANGARA,
        "MAIN_HOST": os.getenv("MAIN_HOST"),
        "MAIN_HOST_SCHEME": os.getenv("MAIN_HOST_SCHEME"),
    }
    return render(request, "manager-page.html", context)


def make_search(request, search):
    """Function make requests to elasticsearch and return json"""

    data = ""
    if re.match(r"^\d{1}", search):
        data = {
            "from": 0,
            "size": 100,
            "query": {
                "bool": {
                    "should": [
                        {"wildcard": {"cat": {"value": f"{search}*"}}},
                        {"wildcard": {"cat2": {"value": f"{search}*"}}},
                    ]
                }
            },
        }
    elif re.match(r"[A-Za-z]+", search):
        data = {
            "from": 0,
            "size": 100,
            "query": {
                "bool": {
                    "should": [
                        {"wildcard": {"cat": {"value": f"{search}*"}}},
                        {"wildcard": {"cat2": {"value": f"{search}*"}}},
                    ]
                }
            },
        }
    else:
        data = {
            "from": 0,
            "size": 200,
            "query": {"match": {"name": {"query": f"{search}", "operator": "and"}}},
        }

    r = json.dumps("")
    if search:
        try:

            r = requests.post(
                f"{settings.ELASTIC_URL}/{settings.ELASTIC_INDEX}/_search",
                auth=HTTPBasicAuth(
                    os.getenv("ELASTIC_USER"), os.getenv("ELASTIC_PASSWORD")
                ),
                headers={"Content-Type": "application/json"},
                data=json.dumps(data),
            )
        except Exception as e:
            return JsonResponse({"code": 500, "message": f"Server error{e}"})

    return JsonResponse(r.json())


def make_search_angara(request, search):
    """Function make requests to elasticsearch and return json"""
    print(search)

    r = requests.get(
        f"{settings.ELASTIC_URL_ANGARA}/api/product/jsontest-get-products-for-angara-procenka/{search}/"
    )
    # print(r.json())

    return JsonResponse(r.json())


def make_total_count(request):
    """Make query for totl count in supplers database"""

    try:
        r = requests.get(
            f"{settings.ELASTIC_URL}/{settings.ELASTIC_INDEX}/_count",
            auth=HTTPBasicAuth(
                os.getenv("ELASTIC_USER"), os.getenv("ELASTIC_PASSWORD")
            ),
            headers={"Content-Type": "application/json"},
        )
    except Exception as e:
        return JsonResponse({"error": e, "message": "Can't request server suppliers"})

    return JsonResponse(r.json())


def make_total_count_angara(request):
    """Make query for totl count in angara database"""

    try:
        r = requests.get(
            f"{settings.ELASTIC_URL_ANGARA}/{settings.ELASTIC_INDEX}/_count"
        )
        # print(r.json())
    except Exception as e:
        return JsonResponse({"error": e, "message": "Can't request server suppliers"})

    return JsonResponse(r.json())
