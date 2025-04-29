from django.db import models

# Create your models here.
class Artist(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	bio =  models.TextField()

class Genre(models.Model):
	title = models.CharField(max_length = 30)


class Production(models.Model):
	name = models.CharField(max_length = 30)
	bio = models.TextField()

class Song(models.Model):
	title = models.CharField(max_length = 50)
	release_date = models.DateField()
	duration = models.IntegerField()
	artists = models.ManyToManyField(Artist)
	genres = models.ManyToManyField(Genre)
	production = models.ForeignKey(Production, on_delete = models.CASCADE)


class Playlist(models.Model):
	title = models.CharField(max_length = 30)
	songs = models.ManyToManyField(Song)

