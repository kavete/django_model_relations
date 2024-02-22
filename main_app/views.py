from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main_app.models import Artist, Song
from model_relationships.serializers import ArtistSerializer


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


@api_view(['GET', 'POST'])
def fetch_or_save_artist(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(instance=artists, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Artist saved'})


@api_view(['GET'])
def fetch_artist(request, id):
    artist = Artist.objects.get(pk=id)

    return None


def update_artist(request):
    return None


def delete_artist(request):
    return None


def artist_albums(request):
    return None
