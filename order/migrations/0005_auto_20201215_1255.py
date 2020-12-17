# Generated by Django 3.1.4 on 2020-12-15 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0005_auto_20201214_2115'),
        ('order', '0004_remove_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.billingaddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.shippingaddress'),
        ),
    ]
