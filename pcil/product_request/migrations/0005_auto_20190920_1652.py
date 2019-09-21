# Generated by Django 2.2.2 on 2019-09-20 16:52

from django.db import migrations, models
import django.db.models.deletion
import product_request.models


class Migration(migrations.Migration):

    dependencies = [
        ('product_request', '0004_auto_20190920_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_requisition',
            old_name='name',
            new_name='customer_name',
        ),
        migrations.RemoveField(
            model_name='product_requisition',
            name='product_ids',
        ),
        migrations.AddField(
            model_name='product_requisition',
            name='sub_product_id',
            field=models.ForeignKey(default=product_request.models.product_requisition.get_default, on_delete=django.db.models.deletion.CASCADE, to='product_request.pcil_products'),
        ),
    ]