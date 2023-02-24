from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login,authenticate  
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect


class LoginUserView(LoginView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username,password=password)
        login(request,user)
        messages.success(request,'you have logged in to your account')
        return super().post(request, *args, **kwargs)

class LogoutUserView(LogoutView):
    next_page = 'auth:login'

class CreateUserView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    
    def post(self, request, *args, **kwargs):
        username = self.request.POST['username']
        email = self.request.POST['email']
        fname = self.request.POST['fName']
        lname = self.request.POST['lName']
        password = self.request.POST['password1']
        passwordConf = self.request.POST['password2']
        if password != passwordConf:
            messages.error(request,'password do not match')
        else:
            user = User.objects.create_user(username=username,email=email,first_name=fname,last_name=lname,password=password)
            user.save()
            messages.success(request,'your account was created succesfully')
            return redirect('auth:login')
        return super().post(request, *args, **kwargs)
    

