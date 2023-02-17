from django.shortcuts import redirect

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView 
# from django.urls import reverse_lazy


# Create your views here.

class UserLoginView(LoginView):
    template_name = "login/login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/user/admin")
        return super().dispatch(request, *args, **kwargs)


class UserLogout(LogoutView):
    template_name = "login/logout.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # pendiente la proxima funcion