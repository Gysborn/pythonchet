from django.contrib import admin

from .models import *


class DjAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'description', 'slag')
    list_display_links = ('id', 'name')
#     # search_fields = ('description')


admin.site.register(Dj)
admin.site.register(Dj272)
admin.site.register(Dj280)
admin.site.register(Dj282)
admin.site.register(Dj291)
admin.site.register(Dj292)
admin.site.register(Dj301)
admin.site.register(Dj302)
admin.site.register(Dj311)
admin.site.register(Dj312)
admin.site.register(Dj320)
