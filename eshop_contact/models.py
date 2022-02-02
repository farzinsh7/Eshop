from django.db import models


class ContactUS(models.Model):
    full_name = models.CharField(max_length=120, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    subject = models.CharField(max_length=200, verbose_name='عنوان پیام')
    text = models.TextField(verbose_name='متن پیام')
    is_read = models.BooleanField(verbose_name='خوانده شده / نشده', default=False)

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return self.full_name