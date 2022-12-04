from django.core.management.base import BaseCommand, CommandError
from data.views import get_suppliers
from django.core.mail import send_mail
from django.conf import settings


class Command(BaseCommand):
    help = "Getting prices for all suppliers"

    def handle(self, *args, **options):

        try:
            message = get_suppliers(None)
            send_mail(
                subject="Suppliers Pricess Success",
                message=f"CronJob has finished {message}",
                from_email="priceMachine@sendblue.com",
                recipient_list=["angara99@gmail.com"],
                fail_silently=False,
            )
        except:
            send_mail(
                subject="Suppliers Pricess Error",
                message="CronJob has finished With error",
                from_email="priceMachine@sendblue.com",
                recipient_list=["angara99@gmail.com"],
                fail_silently=False,
            )
        # return super().handle(*args, **options)
