from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import format_html
from .models import *

admin.site.register(Song)
admin.site.register(Video)
admin.site.register(Application)
admin.site.register(Concert)
admin.site.register(News)

class PhotoAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_tag')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

admin.site.register(Photo, PhotoAdmin)
