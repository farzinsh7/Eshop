from django.db import models
from eshop_products.models import get_filename_ext
from django.core.files.storage import FileSystemStorage
import unicodedata


def upload_image_path(instance, filename):
    final_name = f"{instance.id}-{instance.siteTitle}"
    return f"setting/{final_name}"


# Create your models here.
class SiteSetting(models.Model):
    siteTitle = models.CharField(max_length=150, verbose_name='عنوان سایت')
    logo_image = models.ImageField(upload_to=upload_image_path, verbose_name='لوگو سایت', null=True)
    address = models.CharField(max_length=400, verbose_name='آدرس')
    phone = models.CharField(max_length=50, verbose_name='تلفن')
    mobile = models.CharField(max_length=50, verbose_name='تلفن همراه')
    fax = models.CharField(max_length=50, verbose_name='فکس')
    email = models.EmailField(max_length=50, verbose_name='ایمیل')
    about_us = models.TextField(verbose_name='درباره ما', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'مدیریت تنظیمات'
        verbose_name = 'تنظیمات سایت'

    def __str__(self):
        return self.siteTitle


# session 63
class ASCIIFileSystemStorage(FileSystemStorage):
    """
    Convert unicode characters in name to ASCII characters.
    """

    def get_valid_name(self, name):
        name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore')
        return super(ASCIIFileSystemStorage, self).get_valid_name(name)
