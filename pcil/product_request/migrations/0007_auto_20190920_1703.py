# Generated by Django 2.2.2 on 2019-09-20 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_request', '0006_auto_20190920_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_requisition',
            old_name='sub_product_id',
            new_name='super_product_id',
        ),
        migrations.AddField(
            model_name='product_requisition',
            name='sub_product_name',
            field=models.CharField(default='Termite', max_length=1000, unique=True),
        ),
    ]
