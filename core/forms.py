from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado, VideoJuego, Resena


class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'email', 'telefono', 'foto_perfil', 'password1', 'password2']


class VideoJuegoForm(forms.ModelForm):
    class Meta:
        model = VideoJuego
        fields = [
            'titulo',
            'descripcion',
            'fecha_lanzamiento',
            'precio',
            'imagen',
            'categoria',
            'desarrolladora',
            'plataformas',
        ]
        widgets = {
            'fecha_lanzamiento': forms.DateInput(attrs={'type': 'date'}),
        }


class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['videojuego', 'comentario', 'puntuacion']