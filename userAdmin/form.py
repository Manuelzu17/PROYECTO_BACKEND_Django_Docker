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


