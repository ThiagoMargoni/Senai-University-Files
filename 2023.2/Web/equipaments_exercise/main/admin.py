from django.contrib import admin
from .models import *

class detEquipament(admin.ModelAdmin):
    list_display = [f.name for f in Equipament._meta.get_fields()]
    list_display_links = ('id','name',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Equipament, detEquipament)

class detComments(admin.ModelAdmin):
    list_display= [f.name for f in Comment._meta.get_fields()]
    list_display_links = ('id','comment',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Comment, detComments)