# Generated by Django 4.2.11 on 2024-04-11 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0009_goods_browsers_goods_order"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="goods",
            name="order",
        ),
    ]