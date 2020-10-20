from django import forms
from .models import Musicas
class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musicas
        fields = {
            'titulo',
            'album',
            'segundos',
            }


        