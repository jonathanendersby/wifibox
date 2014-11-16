from django.contrib import admin

from core.models import Media, MediaType, MediaCategory

admin.site.register(Media)
admin.site.register(MediaType)
admin.site.register(MediaCategory)
