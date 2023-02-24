from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import CreateView



class LoginUserView(LoginView):
    template_name = 'login.html'

class CreateUserView(LoginView):
    template_name = 'register.html'
