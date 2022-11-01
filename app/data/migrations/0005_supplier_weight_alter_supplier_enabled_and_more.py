# Generated by Django 4.1.2 on 2022-10-31 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0004_supplier_skip_rows"),
    ]

    operations = [
        migrations.AddField(
            model_name="supplier",
            name="weight",
            field=models.IntegerField(default=100, help_text="Вес поставщика"),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="enabled",
            field=models.BooleanField(
                default=True, help_text="Показывать поставщика или нет"
            ),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="name",
            field=models.CharField(
                help_text="Наименование поставщика, английскими буквами без пробелов",
                max_length=255,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="price_fields",
            field=models.TextField(
                blank=True, help_text="Поля в прайсе в фомате json", null=True
            ),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="skip_rows",
            field=models.IntegerField(
                blank=True, help_text="Сколько строк пропустить сверху", null=True
            ),
        ),
    ]