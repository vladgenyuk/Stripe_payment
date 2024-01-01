from django.contrib import admin
from .models import Product, Order, Tax, Discount


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'currency')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_total')
    filter_horizontal = ('products',)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'amount')


class TaxAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'amount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Tax, TaxAdmin)
