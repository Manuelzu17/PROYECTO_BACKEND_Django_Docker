"""backend_proyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# login app
from userAdmin.views import UserAdmin, ComentarioCreateView, RespuestaCreateView, ComentarioListView,ComentarioUpdateView, IndividualDetailView, discusionesListView
from loginU.views import UserLoginView, UserLogout
from home.views import HomeView

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.as_view(), name="login"),
    path('user/admin/', discusionesListView.as_view(), name="usersAdmin"),
    path('discusiones/', discusionesListView.as_view(), name="discuciones"),
    path('accounts/profile/', discusionesListView.as_view(), name="usersAdmin"),
    path('logout/', UserLogout.as_view(), name="logout"),
    path('comentarios/', ComentarioListView.as_view(), name='lista_comentarios'),
    path('crear_comentario/', ComentarioCreateView.as_view(template_name='userAdmin/create.html'), name='crear_comentario'),
    path('comentario/<int:pk>/editar/', ComentarioUpdateView.as_view(), name='editar_comentario'),
    path('crear_respuesta/<int:comentario_id>/', RespuestaCreateView.as_view(), name='crear_respuesta'),
    path('Individual/<int:pk>/', IndividualDetailView.as_view(), name='Individual'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
