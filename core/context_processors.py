from .models import Categoria


def categorias_context(request):
    return {
        'categorias_nav': Categoria.objects.all()
    }