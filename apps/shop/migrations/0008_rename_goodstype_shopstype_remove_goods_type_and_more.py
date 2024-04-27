# Generated by Django 4.2.11 on 2024-04-06 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0007_goodstype_goods_type"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="GoodsType",
            new_name="ShopsType",
        ),
        migrations.RemoveField(
            model_name="goods",
            name="type",
        ),
        migrations.AddField(
            model_name="shop",
            name="types",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="type",
                to="shop.shopstype",
                verbose_name="类型",
            ),
        ),
        migrations.AlterModelTable(
            name="shopstype",
            table="Shops_type",
        ),
    ]
