from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'aboutus.html'

class ProductPageView(TemplateView):
    template_name = 'product.html'
