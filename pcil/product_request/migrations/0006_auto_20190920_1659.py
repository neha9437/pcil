# Generated by Django 2.2.2 on 2019-09-20 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_request', '0005_auto_20190920_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_requisition',
            name='citi_id',
        ),
        migrations.RemoveField(
            model_name='product_requisition',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='product_requisition',
            name='phone_number',
        ),
    ]
