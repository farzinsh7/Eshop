# Generated by Django 3.2 on 2021-04-20 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ref_id',
            field=models.CharField(default='******', max_length=200, verbose_name='کد رهگیری'),
        ),
    ]