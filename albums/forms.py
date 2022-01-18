from django.forms import ModelForm
from .models import Album

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['title_name', 'artist_name', 'created_at', 'length_in_minutes',]