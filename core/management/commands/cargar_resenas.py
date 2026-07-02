import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from core.models import VideoJuego, Resena


class Command(BaseCommand):
    help = 'Carga reseñas de prueba para los videojuegos'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        grupo_usuarios, _ = Group.objects.get_or_create(name='Usuarios')

        usuarios_data = [
            ('lautaro', 'lautaro@mail.com'),
            ('sofia', 'sofia@mail.com'),
            ('martin', 'martin@mail.com'),
            ('valentina', 'valentina@mail.com'),
            ('tomas', 'tomas@mail.com'),
        ]

        usuarios = []

        for username, email in usuarios_data:
            usuario, creado = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': email
                }
            )

            if creado:
                usuario.set_password('usuario12345')
                usuario.save()

            usuario.groups.add(grupo_usuarios)
            usuarios.append(usuario)

        videojuegos = list(VideoJuego.objects.all())

        if not videojuegos:
            self.stdout.write(self.style.WARNING('No hay videojuegos cargados. Primero ejecutá cargar_catalogo.'))
            return

        comentarios = [
            'Muy buen juego, tiene una jugabilidad entretenida y una historia interesante.',
            'Me gustó bastante, aunque algunas partes se sienten repetitivas.',
            'Excelente apartado visual y muy buena ambientación.',
            'Es un juego recomendable para pasar muchas horas explorando.',
            'La dificultad está bien lograda y mantiene el desafío.',
            'Tiene buenos personajes y una experiencia bastante completa.',
            'Me pareció divertido, ideal para jugar con amigos.',
            'La historia es atrapante y el diseño de niveles está muy bien hecho.',
            'Buen juego, aunque podría mejorar en algunos detalles técnicos.',
            'Una experiencia muy recomendable dentro de su género.',
            'Tiene buena música, buenos gráficos y una jugabilidad sólida.',
            'No es perfecto, pero cumple muy bien con lo que propone.',
        ]

        cantidad = 0

        for videojuego in videojuegos:
            for _ in range(2):
                usuario = random.choice(usuarios)
                comentario = random.choice(comentarios)
                puntuacion = random.randint(6, 10)

                Resena.objects.create(
                    usuario=usuario,
                    videojuego=videojuego,
                    comentario=comentario,
                    puntuacion=puntuacion
                )

                cantidad += 1

        self.stdout.write(self.style.SUCCESS(f'Se cargaron {cantidad} reseñas correctamente.'))