# Generated by Django 3.2 on 2021-04-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0002_auto_20210417_1518'),
        ('eshop_tag', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'برچسب', 'verbose_name_plural': 'برچسب ها'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیر فعال'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(blank=True, to='eshop_products.Product', verbose_name='محصولات'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=120, verbose_name='عنوان'),
        ),
    ]
