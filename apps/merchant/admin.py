from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    model = Merchant
    list_display = ['merchantmen', 'email', 'mobile']