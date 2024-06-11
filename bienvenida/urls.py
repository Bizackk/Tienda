# bienvenida/urls.py

from django.urls import path
from . import views as bienvenida_views  

urlpatterns = [
    path('', bienvenida_views.bienvenida, name='bienvenida'),
    path('registro/', bienvenida_views.registro, name='registro'),
    path('login/', bienvenida_views.login, name='login'),
    path('cerrarSesion/', bienvenida_views.cerrarSesion, name='cerrarSesion'),
]