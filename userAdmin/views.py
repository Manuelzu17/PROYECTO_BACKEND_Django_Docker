from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
class UserAdmin(TemplateView):
    template_name = "userAdmin/UserAdmin.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        print(request.method.lower())
        return super().dispatch(request, *args, **kwargs)