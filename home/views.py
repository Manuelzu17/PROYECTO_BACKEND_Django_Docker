from django.shortcuts import render
from django.views.generic import TemplateView
from userAdmin.models import Producto, Comentario
from django.views.generic.list import ListView

# Create your views here.
class HomeView(ListView):
    model = Comentario
    template_name = "home/home.html" #your_template

