from django.http import HttpResponse
from django.shortcuts import render

from main_app.models import Artist, Song


# Create your views here.
def show(request):
    # artist = Artist.objects.order_by('?').first()
    # print(artist)
    # albums = artist.album_set.all()
    # print(albums)
    # for album in albums:
    #     print(f'Album:  {album.name} {album.release_year}')
    #     songs = album.songs.all()
    #     print(len(songs), "Songs")
    #     for song in songs:
    #         print(f'Song: {song.name} {song.duration}')

    song = Song.objects.order_by('?').first()
    print(song)
    album = song.album
    print(album)
    artists = album.artists.all().values('name')
    print(artists)
    return HttpResponse(artists)
