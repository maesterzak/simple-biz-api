# Generated by Django 4.1.1 on 2022-09-22 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_datetime_orders_date_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderItems',
        ),
    ]
