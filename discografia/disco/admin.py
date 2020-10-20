from django.contrib import admin
from .models import Albuns, Musicas, Bandas

class AlbunsAdmin(admin.ModelAdmin):
    list_display = [
        'titulo',
        'banda',
        ]
    list_display_links = [
        'titulo'
        ]
    list_editable = [
        'banda'
        ]
class MusicasAdmin(admin.ModelAdmin):
    list_display = [
        'titulo',
        'album',
        'segundos'
        ]
    list_display_links = [
        'album'
        ]
    list_editable = [
        'titulo',
        'segundos'
        ]

   
admin.site.register(Albuns, AlbunsAdmin)
admin.site.register(Musicas, MusicasAdmin)
admin.site.register(Bandas)