# Generated by Django 4.2.11 on 2024-03-30 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_goods_shop_goods"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="goods",
            options={"verbose_name": "产品", "verbose_name_plural": "产品"},
        ),
        migrations.AlterModelTable(
            name="goods",
            table="shop_goods",
        ),
    ]
