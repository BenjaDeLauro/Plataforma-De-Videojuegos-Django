from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Crea grupos y permisos iniciales para GameHub'

    def handle(self, *args, **kwargs):
        grupo_usuarios, creado = Group.objects.get_or_create(name='Usuarios')
        grupo_editores, creado = Group.objects.get_or_create(name='Editores')
        grupo_admins, creado = Group.objects.get_or_create(name='Administradores GameHub')

        permisos_usuarios = [
            'view_videojuego',
            'view_resena',
            'add_resena',
        ]

        permisos_editores = [
            'view_videojuego',
            'add_videojuego',
            'change_videojuego',
            'delete_videojuego',
            'view_resena',
            'add_resena',
            'change_resena',
            'delete_resena',
        ]

        permisos_admins = [
            'view_videojuego',
            'add_videojuego',
            'change_videojuego',
            'delete_videojuego',
            'view_resena',
            'add_resena',
            'change_resena',
            'delete_resena',
            'view_categoria',
            'add_categoria',
            'change_categoria',
            'delete_categoria',
            'view_plataforma',
            'add_plataforma',
            'change_plataforma',
            'delete_plataforma',
            'view_desarrolladora',
            'add_desarrolladora',
            'change_desarrolladora',
            'delete_desarrolladora',
            'view_biblioteca',
            'add_biblioteca',
            'change_biblioteca',
            'delete_biblioteca',
        ]

        self.asignar_permisos(grupo_usuarios, permisos_usuarios)
        self.asignar_permisos(grupo_editores, permisos_editores)
        self.asignar_permisos(grupo_admins, permisos_admins)

        self.stdout.write(self.style.SUCCESS('Grupos y permisos creados correctamente.'))

    def asignar_permisos(self, grupo, permisos):
        grupo.permissions.clear()

        for codename in permisos:
            permiso = Permission.objects.filter(codename=codename).first()

            if permiso:
                grupo.permissions.add(permiso)