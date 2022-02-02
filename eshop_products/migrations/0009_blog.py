# Generated by Django 3.2 on 2021-05-11 09:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0008_alter_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]