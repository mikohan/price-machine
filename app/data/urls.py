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
)
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    path("emails/", get_emails, name="get-emails"),
    path("supplier/<int:pk>/", get_supplier, name="get-supplier-price"),
    path("suppliers/", list_suppliers, name="list-suppliers"),
    path("ajax-update-suppliers/", get_suppliers, name="ajax-update-suppliers"),
    path("ajax-update-supplier/", ajax_upate_supplier, name="ajax-update-supplier"),
    path("transform-price/", transform_prices, name="transform-price"),
    path("experiment", experiment, name="experiment"),
    # Elasticsearch requests
    path("search/<str:search>/", make_search, name="make-search"),
    path("search-angara/<str:search>/", make_search_angara, name="make-search-angara"),
    path("total-count/", make_total_count, name="make-total-count"),
    path(
        "total-count-angara/", make_total_count_angara, name="make-total-count-angara"
    ),
]
