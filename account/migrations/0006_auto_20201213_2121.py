# Generated by Django 3.1.4 on 2020-12-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20201213_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=12, verbose_name='phone number'),
        ),
    ]
