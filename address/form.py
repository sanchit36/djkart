from django import forms
from .models import ShippingAddress, BillingAddress
from account.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        exclude = ['customer']
        widgets = {
            'address_s': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234 Main St'}),
            'state_s': forms.Select(attrs={'class': 'custom-select d-block w-100'}),
            'zip_code_s': forms.TextInput(attrs={'class': 'form-control'}),
            'city_s': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = '__all__'
        exclude = ['customer']
        widgets = {
            'address_b': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234 Main St'}),
            'state_b': forms.Select(attrs={'class': 'custom-select d-block w-100'}),
            'zip_code_b': forms.TextInput(attrs={'class': 'form-control'}),
            'city_b': forms.TextInput(attrs={'class': 'form-control'}),
        }
