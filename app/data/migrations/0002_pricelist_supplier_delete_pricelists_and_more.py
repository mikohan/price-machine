# Generated by Django 4.1.2 on 2022-10-31 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PriceList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                ("brand", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "original_number",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("oem_number", models.CharField(blank=True, max_length=255, null=True)),
                ("stock", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("updated_price", models.DateField(blank=True)),
                ("price_fields", models.TextField(blank=True, null=True)),
            ],
            options={"verbose_name": "Поставщик", "verbose_name_plural": "Поставщики",},
        ),
        migrations.DeleteModel(name="PriceLists",),
        migrations.AddField(
            model_name="pricelist",
            name="supplier",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="data.supplier"
            ),
        ),
    ]
