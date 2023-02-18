from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)


class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    asunto = models.CharField(max_length=200)
    comentario = models.TextField()
    imagen = ResizedImageField(size=[800, 600], quality=90, upload_to='db/')

class Respuesta(models.Model):
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='respuestas')
    nombre = models.CharField(max_length=100)
    respuesta = models.TextField()