from django.db import models
from account.models import Customer
from django.utils.text import gettext_lazy as _


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    address_s = models.CharField(max_length=255)
    state_s = models.ForeignKey(
        State, on_delete=models.SET_NULL, null=True)
    city_s = models.CharField(max_length=150)
    zip_code_s = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'Shipping addresses'

    def __str__(self):
        return self.address_s


class BillingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    address_b = models.CharField(max_length=255)
    state_b = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city_b = models.CharField(max_length=150)
    zip_code_b = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'Billing addresses'

    def __str__(self):
        return self.address_b
