from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class UsuarioPersonalizado(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='usuarios/', blank=True, null=True)

    def __str__(self):
        return self.username


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Desarrolladora(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre


class VideoJuego(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_lanzamiento = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='videojuegos/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='videojuegos')
    desarrolladora = models.ForeignKey(Desarrolladora, on_delete=models.CASCADE, related_name='videojuegos')
    plataformas = models.ManyToManyField(Plataforma, related_name='videojuegos')

    def __str__(self):
        return self.titulo


class Resena(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resenas')
    videojuego = models.ForeignKey(VideoJuego, on_delete=models.CASCADE, related_name='resenas')
    comentario = models.TextField()
    puntuacion = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.videojuego} - {self.usuario}'


class Biblioteca(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='biblioteca')
    videojuego = models.ForeignKey(VideoJuego, on_delete=models.CASCADE, related_name='bibliotecas')
    agregado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'videojuego')

    def __str__(self):
        return f'{self.usuario} tiene {self.videojuego}'