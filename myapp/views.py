from django.shortcuts import render, redirect, get_object_or_404
from .models import Artist, Production, Genre, Song, Playlist
from django.contrib import messages

def create_song(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        released_date = request.POST.get('released_date')
        duration = request.POST.get('duration')
        production_id = request.POST.get('production')
        artist_ids = request.POST.getlist('artists')
        genre_ids = request.POST.getlist('genres')

        try:
            production = Production.objects.get(id=production_id)
            song = Song.objects.create(
                title=title,
                released_date=released_date,
                duration=duration,
                production=production
            )

            for artist_id in artist_ids:
                artist = Artist.objects.get(id=artist_id)
                song.artists.add(artist)

            for genre_id in genre_ids:
                genre = Genre.objects.get(id=genre_id)
                song.genres.add(genre)

            messages.success(request, 'Song created successfully!')
            return redirect('fetch_songs')

        except Exception as e:
            messages.error(request, f'Error creating song: {str(e)}')
            return redirect('song_form')

    artists = Artist.objects.all()
    genres = Genre.objects.all()
    productions = Production.objects.all()
    context = {
        'artists': artists,
        'genres': genres,
        'productions': productions
    }
    return render(request, 'song_form.html', context)

def fetch_songs(request):
    songs = Song.objects.all()
    context = {'songs': songs}
    return render(request, 'songs.html', context)

def delete_song(request, id):
    song = get_object_or_404(Song, id=id)
    song.delete()
    messages.success(request, 'Song deleted successfully!')
    return redirect('fetch_songs')

def edit_song(request, id):
    song = get_object_or_404(Song, id=id)
    
    if request.method == 'POST':
        song.title = request.POST.get('title')
        song.released_date = request.POST.get('released_date')
        song.duration = request.POST.get('duration')
        production_id = request.POST.get('production')
        artist_ids = request.POST.getlist('artists')
        genre_ids = request.POST.getlist('genres')

        try:
            song.production = Production.objects.get(id=production_id)
            song.save()

            song.artists.clear()
            for artist_id in artist_ids:
                artist = Artist.objects.get(id=artist_id)
                song.artists.add(artist)

            song.genres.clear()
            for genre_id in genre_ids:
                genre = Genre.objects.get(id=genre_id)
                song.genres.add(genre)

            messages.success(request, 'Song updated successfully!')
            return redirect('fetch_songs')

        except Exception as e:
            messages.error(request, f'Error updating song: {str(e)}')
            return redirect('edit_song', id=id)

    artists = Artist.objects.all()
    genres = Genre.objects.all()
    productions = Production.objects.all()
    context = {
        'song': song,
        'artists': artists,
        'genres': genres,
        'productions': productions
    }
    return render(request, 'edit_song.html', context)

def create_artist(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        bio = request.POST.get('bio')
        
        try:
            Artist.objects.create(
                first_name=first_name,
                last_name=last_name,
                bio=bio
            )
            messages.success(request, 'Artist created successfully!')
            return redirect('fetch_artist')
        except Exception as e:
            messages.error(request, f'Error creating artist: {str(e)}')
            return redirect('create_artist')
    
    return render(request, 'artist_pages/create_artist.html')

def fetch_artist(request):
    artists = Artist.objects.all()
    context = {'singers': artists}
    return render(request, "artist_pages/artist.html", context)

def delete_artist(request, id):
    artist = get_object_or_404(Artist, id=id)
    artist.delete()
    messages.success(request, 'Artist deleted successfully!')
    return redirect('fetch_artist')

def edit_artist(request, id):
    artist = get_object_or_404(Artist, id=id)
    if request.method == 'POST':
        artist.first_name = request.POST.get('first_name')
        artist.last_name = request.POST.get('last_name')
        artist.bio = request.POST.get('bio')
        
        try:
            artist.save()
            messages.success(request, 'Artist updated successfully!')
            return redirect('fetch_artist')
        except Exception as e:
            messages.error(request, f'Error updating artist: {str(e)}')
            return redirect('edit_artist', id=id)
    
    return render(request, 'artist_pages/edit_artist.html', {'artist': artist})

def fetch_production(request):
    productions = Production.objects.all()
    context = {'productions': productions}
    return render(request, 'production.html', context)

def create_production(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        
        try:
            Production.objects.create(name=name, bio=bio)
            messages.success(request, 'Production created successfully!')
            return redirect('fetch_production')
        except Exception as e:
            messages.error(request, f'Error creating production: {str(e)}')
            return redirect('create_production')
    
    return render(request, 'create_production.html')

def edit_production(request, id):
    production = get_object_or_404(Production, id=id)
    
    if request.method == 'POST':
        production.name = request.POST.get('name')
        production.bio = request.POST.get('bio')
        
        try:
            production.save()
            messages.success(request, 'Production updated successfully!')
            return redirect('fetch_production')
        except Exception as e:
            messages.error(request, f'Error updating production: {str(e)}')
            return redirect('edit_production', id=id)
    
    context = {'production': production}
    return render(request, 'edit_production.html', context)

def delete_production(request, id):
    production = get_object_or_404(Production, id=id)
    production.delete()
    messages.success(request, 'Production deleted successfully!')
    return redirect('fetch_production')

def fetch_genre(request):
    genres = Genre.objects.all()
    context = {'genres': genres}
    return render(request, 'genre/genre.html', context)

def create_genre(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        try:
            Genre.objects.create(name=name)
            messages.success(request, 'Genre created successfully!')
            return redirect('fetch_genre')
        except Exception as e:
            messages.error(request, f'Error creating genre: {str(e)}')
            return redirect('create_genre')
    
    return render(request, 'genre/create_genre.html')

def edit_genre(request, id):
    genre = get_object_or_404(Genre, id=id)
    
    if request.method == 'POST':
        genre.name = request.POST.get('name')
        
        try:
            genre.save()
            messages.success(request, 'Genre updated successfully!')
            return redirect('fetch_genre')
        except Exception as e:
            messages.error(request, f'Error updating genre: {str(e)}')
            return redirect('edit_genre', id=id)
    
    context = {'genre': genre}
    return render(request, 'genre/edit_genre.html', context)

def delete_genre(request, id):
    genre = get_object_or_404(Genre, id=id)
    genre.delete()
    messages.success(request, 'Genre deleted successfully!')
    return redirect('fetch_genre')

def playlists(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlist/playlist_list.html', {'playlists': playlists})

def create_playlist(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        song_ids = request.POST.getlist('songs')
        
        if not title:
            messages.error(request, 'Playlist title is required')
            return redirect('create_playlist')
        
        playlist = Playlist.objects.create(title=title)
        if song_ids:
            playlist.songs.set(song_ids)
        
        messages.success(request, 'Playlist created successfully')
        return redirect('playlists')
    
    songs = Song.objects.all()
    return render(request, 'playlist/playlist_form.html', {'songs': songs})

def edit_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        song_ids = request.POST.getlist('songs')
        
        if not title:
            messages.error(request, 'Playlist title is required')
            return redirect('edit_playlist', playlist_id=playlist_id)
        
        playlist.title = title
        playlist.save()
        playlist.songs.set(song_ids)
        
        messages.success(request, 'Playlist updated successfully')
        return redirect('playlists')
    
    songs = Song.objects.all()
    return render(request, 'playlist/playlist_form.html', {
        'playlist': playlist,
        'songs': songs
    })

def delete_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    
    if request.method == 'POST':
        playlist.delete()
        messages.success(request, 'Playlist deleted successfully')
        return redirect('playlists')
    
    return render(request, 'playlist/playlist_confirm_delete.html', {'playlist': playlist})


