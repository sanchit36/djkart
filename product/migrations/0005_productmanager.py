# Generated by Django 3.1.4 on 2020-12-14 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20201213_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]