from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from authUser.views import LoginUserView,LoginView

class HomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'

class AboutPageView(LoginRequiredMixin,TemplateView):
    template_name = 'aboutus.html'
    

class ProductPageView(LoginRequiredMixin,TemplateView):
    template_name = 'product.html'
    
