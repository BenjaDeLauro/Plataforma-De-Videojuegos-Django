from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    UsuarioPersonalizado,
    Categoria,
    Plataforma,
    Desarrolladora,
    VideoJuego,
    Resena,
    Biblioteca,
)


@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(UserAdmin):
    list_display = ('username', 'email', 'telefono', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'telefono')
    list_filter = ('is_staff', 'is_active', 'groups')

    fieldsets = UserAdmin.fieldsets + (
        ('Datos extra', {'fields': ('telefono', 'foto_perfil')}),
    )


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Desarrolladora)
class DesarrolladoraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    search_fields = ('nombre', 'pais')
    list_filter = ('pais',)
    ordering = ('nombre',)


@admin.register(VideoJuego)
class VideoJuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'desarrolladora', 'precio', 'fecha_lanzamiento')
    search_fields = ('titulo', 'descripcion', 'desarrolladora__nombre')
    list_filter = ('categoria', 'desarrolladora', 'plataformas')
    ordering = ('titulo',)


@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('videojuego', 'usuario', 'puntuacion', 'fecha')
    search_fields = ('videojuego__titulo', 'usuario__username', 'comentario')
    list_filter = ('puntuacion', 'fecha')
    ordering = ('-fecha',)


@admin.register(Biblioteca)
class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'videojuego', 'agregado_en')
    search_fields = ('usuario__username', 'videojuego__titulo')
    list_filter = ('agregado_en',)
    ordering = ('-agregado_en',)