from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import VideoJuego, Resena
from .forms import RegistroUsuarioForm, VideoJuegoForm, ResenaForm


class InicioView(TemplateView):
    template_name = 'inicio.html'


class RegistroView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        usuario = form.save()
        login(self.request, usuario)
        return redirect(self.success_url)


class VideoJuegoListView(LoginRequiredMixin, ListView):
    model = VideoJuego
    template_name = 'videojuegos/videojuego_list.html'
    context_object_name = 'videojuegos'


class VideoJuegoDetailView(LoginRequiredMixin, DetailView):
    model = VideoJuego
    template_name = 'videojuegos/videojuego_detail.html'
    context_object_name = 'videojuego'


class VideoJuegoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = VideoJuego
    form_class = VideoJuegoForm
    template_name = 'videojuegos/videojuego_form.html'
    success_url = reverse_lazy('videojuego_list')
    permission_required = 'core.add_videojuego'
    raise_exception = True


class VideoJuegoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = VideoJuego
    form_class = VideoJuegoForm
    template_name = 'videojuegos/videojuego_form.html'
    success_url = reverse_lazy('videojuego_list')
    permission_required = 'core.change_videojuego'
    raise_exception = True


class VideoJuegoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = VideoJuego
    template_name = 'videojuegos/videojuego_confirm_delete.html'
    success_url = reverse_lazy('videojuego_list')
    permission_required = 'core.delete_videojuego'
    raise_exception = True


class ResenaListView(LoginRequiredMixin, ListView):
    model = Resena
    template_name = 'resenas/resena_list.html'
    context_object_name = 'resenas'


class ResenaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Resena
    form_class = ResenaForm
    template_name = 'resenas/resena_form.html'
    success_url = reverse_lazy('resena_list')
    permission_required = 'core.add_resena'
    raise_exception = True

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class ResenaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Resena
    form_class = ResenaForm
    template_name = 'resenas/resena_form.html'
    success_url = reverse_lazy('resena_list')
    permission_required = 'core.change_resena'
    raise_exception = True


class ResenaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Resena
    template_name = 'resenas/resena_confirm_delete.html'
    success_url = reverse_lazy('resena_list')
    permission_required = 'core.delete_resena'
    raise_exception = True