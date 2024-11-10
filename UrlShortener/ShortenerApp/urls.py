from django.urls import path, include
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("", views.home, name="home"),
    path('<str:code>/', views.ShortUrl, name='ShortUrl'),
]