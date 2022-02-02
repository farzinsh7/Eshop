from django.contrib import admin
from .models import Product, ProductsGallery, Blog


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active']

    class Meta:
        model = Product


# class ProductGalleryAdmin(admin.ModelAdmin):
#     list_display = ['__str__']
#
#     class Meta:
#         model = ProductsGallery


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductsGallery)
admin.site.register(Blog)
