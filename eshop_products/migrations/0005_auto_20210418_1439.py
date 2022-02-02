# Generated by Django 3.2 on 2021-04-18 10:09

from django.db import migrations, models
import django.db.models.deletion
import eshop_products.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0004_productsgallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsgallery',
            name='image',
            field=models.ImageField(upload_to=eshop_products.models.upload_gallery_image_path, verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='productsgallery',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_products.product', verbose_name='محصول'),
        ),
    ]