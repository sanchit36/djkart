from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    phone_number = models.CharField(_('phone number'), max_length=12)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    phone_number = models.CharField(_('phone number'), max_length=12)

    def __str__(self):
        return f"{self.id}~{self.email}~"

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def get_short_name(self):
        return {self.first_name}

    def email_customer(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class GuestUser(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.email
