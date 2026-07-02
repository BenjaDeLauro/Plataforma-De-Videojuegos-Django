from django.core.management.base import BaseCommand
from datetime import date
from decimal import Decimal

from core.models import Categoria, Plataforma, Desarrolladora, VideoJuego


class Command(BaseCommand):
    help = 'Carga datos iniciales para el catálogo de videojuegos'

    def handle(self, *args, **kwargs):
        # Categorías
        accion, _ = Categoria.objects.get_or_create(
            nombre='Acción',
            defaults={'descripcion': 'Juegos con combates, movimiento rápido y desafíos constantes.'}
        )

        aventura, _ = Categoria.objects.get_or_create(
            nombre='Aventura',
            defaults={'descripcion': 'Juegos centrados en exploración, historia y progreso.'}
        )

        rpg, _ = Categoria.objects.get_or_create(
            nombre='RPG',
            defaults={'descripcion': 'Juegos de rol con personajes, niveles y progresión.'}
        )

        deportes, _ = Categoria.objects.get_or_create(
            nombre='Deportes',
            defaults={'descripcion': 'Juegos basados en deportes reales o ficticios.'}
        )

        terror, _ = Categoria.objects.get_or_create(
            nombre='Terror',
            defaults={'descripcion': 'Juegos con suspenso, miedo y ambientación oscura.'}
        )

        carreras, _ = Categoria.objects.get_or_create(
            nombre='Carreras',
            defaults={'descripcion': 'Juegos de conducción y competencia de vehículos.'}
        )

        # Plataformas
        pc, _ = Plataforma.objects.get_or_create(nombre='PC')
        playstation, _ = Plataforma.objects.get_or_create(nombre='PlayStation')
        xbox, _ = Plataforma.objects.get_or_create(nombre='Xbox')
        switch, _ = Plataforma.objects.get_or_create(nombre='Nintendo Switch')

        # Desarrolladoras
        rockstar, _ = Desarrolladora.objects.get_or_create(
            nombre='Rockstar Games',
            defaults={'pais': 'Estados Unidos'}
        )

        fromsoftware, _ = Desarrolladora.objects.get_or_create(
            nombre='FromSoftware',
            defaults={'pais': 'Japón'}
        )

        ea, _ = Desarrolladora.objects.get_or_create(
            nombre='EA Sports',
            defaults={'pais': 'Estados Unidos'}
        )

        capcom, _ = Desarrolladora.objects.get_or_create(
            nombre='Capcom',
            defaults={'pais': 'Japón'}
        )

        mojang, _ = Desarrolladora.objects.get_or_create(
            nombre='Mojang Studios',
            defaults={'pais': 'Suecia'}
        )

        nintendo, _ = Desarrolladora.objects.get_or_create(
            nombre='Nintendo',
            defaults={'pais': 'Japón'}
        )

        # Videojuegos
        gta, _ = VideoJuego.objects.get_or_create(
            titulo='Grand Theft Auto V',
            defaults={
                'descripcion': 'Videojuego de acción y mundo abierto donde el jugador puede explorar una ciudad, realizar misiones y participar en distintas actividades.',
                'fecha_lanzamiento': date(2013, 9, 17),
                'precio': Decimal('19999.99'),
                'categoria': accion,
                'desarrolladora': rockstar,
            }
        )
        gta.plataformas.set([pc, playstation, xbox])

        elden_ring, _ = VideoJuego.objects.get_or_create(
            titulo='Elden Ring',
            defaults={
                'descripcion': 'Juego de rol y acción en mundo abierto, con combates exigentes, exploración y una ambientación fantástica.',
                'fecha_lanzamiento': date(2022, 2, 25),
                'precio': Decimal('34999.99'),
                'categoria': rpg,
                'desarrolladora': fromsoftware,
            }
        )
        elden_ring.plataformas.set([pc, playstation, xbox])

        fifa, _ = VideoJuego.objects.get_or_create(
            titulo='EA Sports FC 25',
            defaults={
                'descripcion': 'Videojuego deportivo de fútbol con equipos, torneos, modos online y simulación competitiva.',
                'fecha_lanzamiento': date(2024, 9, 27),
                'precio': Decimal('49999.99'),
                'categoria': deportes,
                'desarrolladora': ea,
            }
        )
        fifa.plataformas.set([pc, playstation, xbox, switch])

        resident, _ = VideoJuego.objects.get_or_create(
            titulo='Resident Evil 4 Remake',
            defaults={
                'descripcion': 'Juego de terror y acción donde el jugador debe sobrevivir en escenarios hostiles enfrentando enemigos y resolviendo desafíos.',
                'fecha_lanzamiento': date(2023, 3, 24),
                'precio': Decimal('29999.99'),
                'categoria': terror,
                'desarrolladora': capcom,
            }
        )
        resident.plataformas.set([pc, playstation, xbox])

        minecraft, _ = VideoJuego.objects.get_or_create(
            titulo='Minecraft',
            defaults={
                'descripcion': 'Juego de aventura y construcción donde el jugador puede explorar, crear estructuras, recolectar recursos y sobrevivir.',
                'fecha_lanzamiento': date(2011, 11, 18),
                'precio': Decimal('14999.99'),
                'categoria': aventura,
                'desarrolladora': mojang,
            }
        )
        minecraft.plataformas.set([pc, playstation, xbox, switch])

        mario_kart, _ = VideoJuego.objects.get_or_create(
            titulo='Mario Kart 8 Deluxe',
            defaults={
                'descripcion': 'Juego de carreras arcade con personajes de Nintendo, circuitos variados y competencias multijugador.',
                'fecha_lanzamiento': date(2017, 4, 28),
                'precio': Decimal('39999.99'),
                'categoria': carreras,
                'desarrolladora': nintendo,
            }
        )
        mario_kart.plataformas.set([switch])

        self.stdout.write(self.style.SUCCESS('Catálogo cargado correctamente.'))