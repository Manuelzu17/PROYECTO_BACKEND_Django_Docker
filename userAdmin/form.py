from django.forms import *
from userAdmin.models import *


# Create the form class.

class comentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = [
            'nombre',
            'asunto',
            'comentario',
            'imagen',
        ]
        labels = {
            'nombre': 'nombre realizada',
            'asunto': 'asunto',
            'comentario': 'comentario',
            'imagen': 'imagen',
        }


class RespuestaForm(ModelForm):
    class Meta:
        model = Respuesta
        fields = ['nombre', 'respuesta', 'comentario']
        labels = {
            'nombre': 'Nombre',
            'respuesta': 'Respuesta',
        }
        widgets = {

            'comentario':Select(attrs={
            'class':'custom-select form-control-border',
            'hidden':'hidden'}),
            
        }
