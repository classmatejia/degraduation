from django.contrib import admin
from .models import *
# Register your models here.


class OrdersInline(admin.TabularInline):
    model = Orders
    extra = 0
    fields = ['date', 'is_comment', 'shop', 'goods']
    readonly_fields = ['date', 'is_comment', 'shop', 'goods']


@admin.register(Consumer)
class Consumer(admin.ModelAdmin):
    admin.site.site_title = "后台管理"
    admin.site.site_header = "LocalHubManager"
    model = Consumer
    inlines = [OrdersInline]
    list_display = ['username', 'mobile', 'email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['username', 'mobile', 'email', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'mobile')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    ordering = ['username']


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    model = Orders
    list_display = ['date', 'user', 'is_comment', 'shop']
    list_filter = ['date', 'is_comment']
    search_fields = ['user__username', 'shop__name']
    filter_horizontal = ['goods']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'fk_user', 'mark', 'fk_shop','date']

