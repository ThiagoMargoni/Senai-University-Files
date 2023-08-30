from django.contrib import admin
from .models import *

class detLocations(admin.ModelAdmin):
    list_display = [f.name for f in Location._meta.get_fields()]
    list_display_links = ('id','name',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Location, detLocations)

class detEpisodes(admin.ModelAdmin):
    list_display = [f.name for f in Episode._meta.get_fields()]
    list_display_links = ('id','name',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Episode, detEpisodes)

class detCharacters(admin.ModelAdmin):
    list_display = [f.name for f in Character._meta.get_fields()]
    list_display_links = ('id','name',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Character, detCharacters)