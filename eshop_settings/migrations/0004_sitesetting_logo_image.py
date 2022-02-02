# Generated by Django 3.2 on 2021-04-18 18:41

from django.db import migrations, models
import eshop_settings.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0003_alter_sitesetting_about_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='logo_image',
            field=models.ImageField(null=True, upload_to=eshop_settings.models.upload_image_path, verbose_name='لوگو سایت'),
        ),
    ]