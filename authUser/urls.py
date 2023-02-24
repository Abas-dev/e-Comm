from django.urls import path
from .views import LoginUserView,CreateUserView,LogoutUserView

app_name = 'auth'

urlpatterns = [
    path('login/',LoginUserView.as_view(),name='login'),
    path('register/',CreateUserView.as_view(),name='register'),
    path('logout/',LogoutUserView.as_view(),name='logout'),
]