from django import forms
from order.models import Order


class OrderDeliveryForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ("being_delivered",)
