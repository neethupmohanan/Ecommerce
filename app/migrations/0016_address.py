# Generated by Django 3.2.25 on 2024-07-09 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_cart_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('housename', models.CharField(max_length=50)),
                ('roadname', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
    ]
