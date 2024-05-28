from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida),
    path('registro/', views.registro),
    path('login/', views.login),
]
