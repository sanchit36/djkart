# Generated by Django 3.1.4 on 2020-12-13 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('image', models.ImageField(upload_to='products/')),
                ('short_description', models.TextField(blank=True, max_length=500, null=True)),
                ('long_description', models.TextField(blank=True, null=True)),
                ('is_featured', models.BooleanField(blank=True, default=False, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('breath', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
