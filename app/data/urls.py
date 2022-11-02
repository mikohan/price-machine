from data.views import home, get_emails, transform_prices, get_suppliers, get_supplier
from django.urls import path

urlpatterns = [
    path("", home, name="test-home"),
    path("emails/", get_emails, name="get-emails"),
    path("supplier/<int:pk>/", get_supplier, name="get-emails"),
    path("suppliers/", get_suppliers, name="get-suppliers"),
    path("transform-prices/", transform_prices, name="transform-prices"),
]
