from django.contrib import admin
from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'ref_id', 'ordered_date',
                    'ordered', 'shipping_address', 'billing_address')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product',  'quantity', 'order')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
