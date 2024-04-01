from django.db import models


# Create your models here.
class Goods(models.Model):
    goods_name = models.CharField(max_length=125, verbose_name='品名')
    desc = models.CharField(max_length=300, verbose_name='描述')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'shop_goods'
        verbose_name = '产品'
        verbose_name_plural = verbose_name


class Shop(models.Model):
    Level = (('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5))
    shop_name = models.CharField(max_length=30, verbose_name='店名', unique=True)
    mark = models.CharField(max_length=10, choices=Level, verbose_name='评分')
    adders = models.CharField(max_length=200, verbose_name='地址')
    phone = models.CharField(max_length=15, verbose_name='电话')
    goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'shops'
        verbose_name = '店铺'
        verbose_name_plural = verbose_name