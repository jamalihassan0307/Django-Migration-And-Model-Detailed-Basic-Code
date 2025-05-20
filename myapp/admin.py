from django.contrib import admin

# Register your models here.
from .models import Artist, Genre ,Playlist ,Production, Song
title = "Music App"
site_header = "Music App Admin"
admin.site.site_title = title
admin.site.site_header = site_header
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'bio')
    search_fields = ('first_name', 'last_name')

class SongAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'release_date', 'duration', 'production',"get_artists", 'get_genres')
    
    search_fields = ('title', 'release_date')
    list_filter = ('release_date', 'production')
    filter_horizontal = ('artists', 'genres')
    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
    def get_artists(self, obj):
        return ", ".join([artist.first_name + " " + artist.last_name for artist in obj.artists.all()])

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre)
admin.site.register(Playlist)
admin.site.register(Production)
admin.site.register(Song, SongAdmin)


