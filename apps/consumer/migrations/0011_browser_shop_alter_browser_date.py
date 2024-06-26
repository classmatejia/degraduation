# Generated by Django 4.2.11 on 2024-04-12 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0011_alter_shop_mark"),
        ("consumer", "0010_remove_comment_fk_orders_comment_fk_shop"),
    ]

    operations = [
        migrations.AddField(
            model_name="browser",
            name="shop",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="browsers",
                to="shop.shop",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="browser",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
