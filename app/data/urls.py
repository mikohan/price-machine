from data.views import (
    home,
    get_emails,
    transform_prices,
    get_suppliers,
    get_supplier,
    list_suppliers,
    ajax_upate_supplier,
    experiment,
    make_search,
    make_search_angara,
    make_total_count,
    make_total_count_angara,
    mapping,
)
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(home, login_url="/admin/login/"), name="home"),
    path("mapping/", mapping, name="mapping"),
    # path("emails/", get_emails, name="get-emails"),
    path(
        "supplier/<int:pk>/",
        login_required(get_supplier, login_url="/admin/login/"),
        name="get-supplier-price",
    ),
    path(
        "suppliers/",
        login_required(list_suppliers, login_url="/admin/login/"),
        name="list-suppliers",
    ),
    path(
        "ajax-update-suppliers/",
        login_required(get_suppliers, login_url="/admin/login/"),
        name="ajax-update-suppliers",
    ),
    path(
        "ajax-update-supplier/",
        login_required(ajax_upate_supplier, login_url="/admin/login/"),
        name="ajax-update-supplier",
    ),
    # path("transform-price/", transform_prices, name="transform-price"),
    # path("experiment", experiment, name="experiment"),
    # Elasticsearch requests
    path("search/<str:search>/", make_search, name="make-search"),
    path("search-angara/<str:search>/", make_search_angara, name="make-search-angara"),
    path("total-count/", make_total_count, name="make-total-count"),
    path(
        "total-count-angara/", make_total_count_angara, name="make-total-count-angara"
    ),
]
