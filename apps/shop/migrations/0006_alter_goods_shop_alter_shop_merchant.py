# Generated by Django 4.2.11 on 2024-04-02 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("merchant", "0006_remove_merchant_shop"),
        ("shop", "0005_remove_shop_goods_goods_shop_shop_merchant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goods",
            name="shop",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="goods",
                to="shop.shop",
                verbose_name="Shop",
            ),
        ),
        migrations.AlterField(
            model_name="shop",
            name="merchant",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="merchant",
                to="merchant.merchant",
                verbose_name="merchant",
            ),
        ),
    ]
