# Generated by Django 3.2 on 2021-04-14 10:56

from django.db import migrations, models
import eshop_products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=eshop_products.models.upload_image_path)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
