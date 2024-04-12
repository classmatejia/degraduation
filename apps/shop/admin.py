from django.contrib import admin
from .models import *


@admin.register(ShopsType)
class ShopsTypeAdmin(admin.ModelAdmin):
    # 如果有需要，可以在这里定义 ShopsType 的 admin 配置
    pass


class GoodsInline(admin.TabularInline):
    model = Goods
    extra = 1


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines = [GoodsInline]
    list_display = ['shop_name', 'mark', 'adders', 'phone', 'merchant']
