# Generated by Django 4.1.2 on 2022-11-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0007_alter_supplier_updated_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="supplier",
            name="name_rus",
            field=models.CharField(default="Change me", max_length=255),
        ),
    ]