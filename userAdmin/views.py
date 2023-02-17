from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from userAdmin.models import Producto, Comentario
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from userAdmin.form import *

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
