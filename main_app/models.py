from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, max_length=60)

    # class Meta:
    #     db_table = 'Musicians'

    def __str__(self):
        return self.name


# many to many

class Album(models.Model):
    name = models.CharField(max_length=60)
    release_year = models.IntegerField()
    artists = models.ManyToManyField(Artist)

    def __str__(self):
        return f'Album: {self.name} {self.release_year}'


# One to many Album to Song

class Song(models.Model):
    name = models.CharField(max_length=60)
    duration = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return self.name
# TODO Add one to one
