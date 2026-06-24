from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),

    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('videojuegos/', views.VideoJuegoListView.as_view(), name='videojuego_list'),
    path('videojuegos/<int:pk>/', views.VideoJuegoDetailView.as_view(), name='videojuego_detail'),
    path('videojuegos/crear/', views.VideoJuegoCreateView.as_view(), name='videojuego_create'),
    path('videojuegos/<int:pk>/editar/', views.VideoJuegoUpdateView.as_view(), name='videojuego_update'),
    path('videojuegos/<int:pk>/eliminar/', views.VideoJuegoDeleteView.as_view(), name='videojuego_delete'),

    path('resenas/', views.ResenaListView.as_view(), name='resena_list'),
    path('resenas/crear/', views.ResenaCreateView.as_view(), name='resena_create'),
    path('resenas/<int:pk>/editar/', views.ResenaUpdateView.as_view(), name='resena_update'),
    path('resenas/<int:pk>/eliminar/', views.ResenaDeleteView.as_view(), name='resena_delete'),
]