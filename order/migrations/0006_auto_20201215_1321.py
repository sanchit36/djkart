# Generated by Django 3.1.4 on 2020-12-15 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20201215_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(null=True),
        ),
    ]