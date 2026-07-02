# GameHub - Plataforma de Videojuegos

GameHub es un sistema web desarrollado con **Django** para gestionar un catálogo de videojuegos, usuarios y reseñas.

## Tecnologías

- Python
- Django
- SQLite
- HTML
- CSS
- Django Templates

## Funcionalidades

- Registro de usuarios desde templates.
- Login y logout.
- Usuario personalizado con `AbstractUser`.
- Catálogo de videojuegos.
- Detalle de videojuegos.
- CRUD completo de videojuegos.
- CRUD completo de reseñas.
- Carga de imágenes con `ImageField`.
- Panel de administración de Django.
- Filtros, búsqueda y ordenamiento en el admin.
- Grupos y permisos.
- Vistas protegidas con login y permisos.
- Context processor para mostrar categorías.
- Estilos mediante archivos static.

## Modelos

El sistema cuenta con los siguientes modelos:

- `UsuarioPersonalizado`
- `Categoria`
- `Plataforma`
- `Desarrolladora`
- `VideoJuego`
- `Resena`
- `Biblioteca`

Los modelos están relacionados entre sí. Un videojuego pertenece a una categoría, tiene una desarrolladora, puede estar en varias plataformas y puede recibir reseñas de usuarios.

## Permisos

El sistema utiliza grupos de Django:

- **Usuarios:** pueden ver videojuegos y reseñas.
- **Editores:** pueden crear, editar y eliminar videojuegos y reseñas.
- **Administradores:** tienen control completo desde el panel de administración.

## Instalación

Clonar el repositorio:

```bash
git clone git@github.com:BenjaDeLauro/Plataforma-De-Videojuegos-Django.git
```

Entrar al proyecto:

```bash
cd Plataforma-De-Videojuegos-Django
```

Crear y activar entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Aplicar migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

Crear grupos y cargar datos iniciales:

```bash
python manage.py crear_grupos
python manage.py cargar_catalogo
python manage.py cargar_resenas
```

Crear superusuario:

```bash
python manage.py createsuperuser
```

Ejecutar servidor:

```bash
python manage.py runserver
```

Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

Panel de administración:

```text
http://127.0.0.1:8000/admin/
```

## Capturas

### Inicio

![Inicio](docs/img/Inicio.png)

### Catálogo

![Catálogo](docs/img/Catalogo.png)

### Detalle de videojuego

![Detalle](docs/img/Detalle-Videojuego.png)

### Reseñas

![Reseñas](docs/img/Reseñas.png)

### Login

![Login](docs/img/Login.png)

### Registro

![Registro](docs/img/Registro.png)




