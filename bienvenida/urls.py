# bienvenida/urls.py
from django.urls import path
from bienvenida import views as bienvenida_vies
from home import views as home_views

urlpatterns = [
    path('', bienvenida_vies.bienvenida, name='bienvenida'),
    path('registro/', bienvenida_vies.registro, name='registro'),
    path('login/', bienvenida_vies.login, name='login'),
    path('cerrarSesion/', bienvenida_vies.cerrarSesion, name='cerrarSesion'),
    path('home/', home_views.home, name='home'),
]
