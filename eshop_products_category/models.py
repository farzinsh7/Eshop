from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    name = models.CharField(max_length=120, verbose_name='عنوان در url')


    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title
