# Generated by Django 3.2 on 2021-04-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0002_sitesetting_about_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='about_us',
            field=models.TextField(blank=True, null=True, verbose_name='درباره ما'),
        ),
    ]
