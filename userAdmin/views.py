from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from userAdmin.models import Producto, Comentario
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from userAdmin.form import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class UserAdmin(TemplateView):
    template_name = "userAdmin/UserAdmin.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        print(request.method.lower())
        return super().dispatch(request, *args, **kwargs)

class ComentarioListView(ListView):
    model = Comentario
    form_class = comentarioForm
    template_name = 'userAdmin/UserAdmin.html'

class ComentarioCreateView(CreateView):
    model = Comentario
    fields = ['nombre', 'asunto', 'comentario', 'imagen']
    success_url = reverse_lazy('usersAdmin')

class ComentarioUpdateView(UpdateView):
    model = Comentario
    fields = ['nombre', 'asunto', 'comentario', 'imagen']
    template_name = 'userAdmin/editar_comentario.html'
    success_url = reverse_lazy('usersAdmin')

class RespuestaCreateView(LoginRequiredMixin, CreateView):
    model = Respuesta
    form_class = RespuestaForm
    template_name = 'userAdmin/agregar_respuesta.html'
    success_url = reverse_lazy('usersAdmin')

    def form_valid(self, form):
        comentario_id = self.kwargs.get('comentario_id')
        comentario = get_object_or_404(Comentario, pk=comentario_id)
        form.instance.comentario = comentario
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        comentario = get_object_or_404(Comentario, pk=self.kwargs['comentario_id'])
        initial['comentario'] = comentario
        return initial