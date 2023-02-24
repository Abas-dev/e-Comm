from django.urls import path

from .views import HomePageView,AboutPageView,ProductPageView

app_name = 'base'

urlpatterns = [
    path('',HomePageView.as_view(), name='homePage'),
    path('about/',AboutPageView.as_view(),name='aboutPage'),
    path('product/',ProductPageView.as_view(),name='productPage'),

]   