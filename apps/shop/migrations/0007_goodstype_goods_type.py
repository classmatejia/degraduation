# Generated by Django 4.2.11 on 2024-04-06 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_alter_goods_shop_alter_shop_merchant"),
    ]

    operations = [
        migrations.CreateModel(
            name="GoodsType",
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
                (
                    "main_type",
                    models.CharField(max_length=30, unique=True, verbose_name="类别"),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subs",
                        to="shop.goodstype",
                        verbose_name="父类别",
                    ),
                ),
            ],
            options={
                "verbose_name": "类型",
                "verbose_name_plural": "类型",
                "db_table": "goods_type",
            },
        ),
        migrations.AddField(
            model_name="goods",
            name="type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.goodstype",
            ),
        ),
    ]