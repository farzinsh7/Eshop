# Generated by Django 3.2 on 2021-05-11 09:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0006_product_visit_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
    ]
