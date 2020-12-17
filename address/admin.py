from django.contrib import admin
from .models import State, ShippingAddress, BillingAddress


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'address_s', 'state_s', 'city_s', 'zip_code_s')


class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'address_b', 'state_b', 'city_b', 'zip_code_b')


admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(BillingAddress, BillingAddressAdmin)
admin.site.register(State)
