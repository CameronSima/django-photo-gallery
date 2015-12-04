from django.contrib import admin

from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.models import Gallery
from .models import GalleryExtended


class GalleryExtendedInline(admin.StackedInline):
    model = GalleryExtended
    can_delete = False
    prepopulated_fields = {'girl_slug': ('girl_name',)}

class GalleryAdmin(GalleryAdminDefault):

    """Define our new one-to-one model as an inline of Photologue's Gallery model."""

    inlines = [GalleryExtendedInline, ]
    

admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)