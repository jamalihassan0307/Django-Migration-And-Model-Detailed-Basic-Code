from django import forms
from .models import Artist, Genre, Production, Song, Playlist
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['first_name', 'last_name', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
class GenreForm(forms.Form):
    name = forms.CharField(max_length=30)
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Genre.objects.filter(name=name).exists():
            raise forms.ValidationError("Genre with this name already exists.")
        return name