from django.db import models
from account.models import Customer
from product.models import Product
from address.models import ShippingAddress, BillingAddress


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ref_id = models.CharField(max_length=20)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(null=True)
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        ShippingAddress, on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        BillingAddress, on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.email} ~ {self.ref_id}"

    @property
    def get_cart_items(self):
        total = 0
        items = self.orderitem_set.all()
        for i in items:
            total += i.quantity
        return total

    @property
    def get_cart_total(self):
        total = 0
        items = self.orderitem_set.all()
        for i in items:
            total += i.get_total
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    @property
    def get_total(self):
        total = self.product.get_price * self.quantity
        return total
