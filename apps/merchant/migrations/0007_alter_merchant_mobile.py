# Generated by Django 4.2.11 on 2024-04-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("merchant", "0006_remove_merchant_shop"),
    ]

    operations = [
        migrations.AlterField(
            model_name="merchant",
            name="mobile",
            field=models.CharField(default=None, max_length=30, verbose_name="手机号"),
        ),
    ]
