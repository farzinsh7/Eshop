from django.contrib import admin
# Register your models here.
from eshop_tag.models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'active']

    class Meta:
        model = Tag


admin.site.register(Tag, TagAdmin)
