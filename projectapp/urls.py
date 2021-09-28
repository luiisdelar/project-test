from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profile/', login_required(views.profile), name='profile'),
]