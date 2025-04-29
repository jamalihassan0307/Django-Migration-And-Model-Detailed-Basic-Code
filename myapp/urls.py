from django.urls import path
from . import views

urlpatterns = [
    path('create_song/', views.create_song, name='song_form'),
    path('fetch_songs/', views.fetch_songs, name='fetch_songs'),
    path('songs/<int:id>/edit/', views.edit_song, name='edit_song'),
    path('songs/<int:id>/delete/', views.delete_song, name='delete_song'),

    path('featch_artist/', views.featch_artist, name='featch_artist'),
    path('create_artist/', views.create_artist, name='create_artist'),
    path('artists/<int:id>/edit/', views.edit_artist, name='edit_artist'),
    path('artists/<int:id>/delete/', views.delete_artist, name='delete_artist'),

    path('productions/', views.fetch_production, name='fetch_production'),
    path('create_production/', views.create_production, name='create_production'),
    path('productions/<int:id>/edit/', views.edit_production, name='edit_production'),
    path('productions/<int:id>/delete/', views.delete_production, name='delete_production'),

    path('genres/', views.fetch_genre, name='fetch_genre'),
    path('create_genre/', views.create_genre, name='create_genre'),
    path('genres/<int:id>/edit/', views.edit_genre, name='edit_genre'),
    path('genres/<int:id>/delete/', views.delete_genre, name='delete_genre'),
]
