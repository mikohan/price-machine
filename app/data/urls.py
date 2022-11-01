from data.views import home, get_emails, transform_prices
from django.urls import path

urlpatterns = [
    path("", home, name="test-home"),
    path("emails/", get_emails, name="get-emails"),
    path("transform-prices/", transform_prices, name="transform-prices"),
]
