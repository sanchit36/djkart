from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import User, Customer


class UserCreationForm(forms.Form):
    error_messages = {
        'password_mismatch': 'The two password fields didn’t match.',
    }
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).count() != 0:
            raise ValidationError("email is already taken")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self):
        email = self.cleaned_data['email']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        phone_number = self.cleaned_data['phone_number']
        password = self.cleaned_data['password1']

        user = User.objects.create(
            email=email, first_name=first_name, last_name=last_name, phone_number=phone_number)
        user.set_password(password)
        user.save()

        customer, created = Customer.objects.get_or_create(email=email)
        customer.user = user
        customer.first_name = first_name
        customer.last_name = last_name
        customer.phone_number = phone_number
        customer.save()

        return user


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
