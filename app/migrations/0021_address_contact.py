# Generated by Django 3.2.25 on 2024-07-24 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='contact',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
