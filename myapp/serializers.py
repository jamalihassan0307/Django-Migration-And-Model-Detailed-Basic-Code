from rest_framework import serializers
from .models import Artist, Genre ,Playlist ,Production, Song

class ArtistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artist
		fields = '__all__'
		

