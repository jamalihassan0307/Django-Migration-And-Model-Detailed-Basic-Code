from django.db import models

# Create your models here.
class Artist(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	bio =  models.TextField()
	def __str__(self):
		return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
	name = models.CharField(max_length = 30)
	def __str__(self):
		return self.name


class Production(models.Model):
	name = models.CharField(max_length = 30)
	bio = models.TextField()
	def __str__(self):
		return self.name

class Song(models.Model):
	title = models.CharField(max_length = 50)
	release_date = models.DateField()
	duration = models.IntegerField()
	artists = models.ManyToManyField(Artist)
	genres = models.ManyToManyField(Genre)
	production = models.ForeignKey(Production, on_delete = models.CASCADE)
	def __str__(self):
		return self.title


class Playlist(models.Model):
	title = models.CharField(max_length = 30)
	songs = models.ManyToManyField(Song)
	def __str__(self):
		return self.title

