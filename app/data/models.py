from django.db import models

# Create your models here.


class PriceList(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    brand = models.CharField(max_length=255, null=True, blank=True)
    original_number = models.CharField(max_length=255, null=True, blank=True)
    oem_number = models.CharField(max_length=255, null=True, blank=True)
    oem_number = models.CharField(max_length=255, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    supplier = models.ForeignKey("Supplier", on_delete=models.CASCADE)


class Supplier(models.Model):

    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="Наименование поставщика, английскими буквами без пробелов",
    )
    email = models.EmailField(max_length=255, unique=True)
    updated_price = models.DateTimeField(blank=True)
    price_fields = models.TextField(
        null=True,
        blank=True,
        help_text="Поля в прайсе в фомате json",
    )
    skip_rows = models.IntegerField(
        null=True,
        blank=True,
        help_text="Сколько строк пропустить сверху",
    )
    enabled = models.BooleanField(
        default=True,
        help_text="Показывать поставщика или нет",
    )
    weight = models.IntegerField(default=10, help_text="Вес поставщика")

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return self.name
