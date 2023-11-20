from django.contrib import admin

from main_app.models import Artist, Album, Song


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'release_year']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'album']
