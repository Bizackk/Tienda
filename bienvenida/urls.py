from django.urls import path
from bienvenida import views as home_bienvenida
from home import views as home_views

urlpatterns = [
    path('', home_bienvenida.bienvenida, name='bienvenida'),
    path('registro/', home_bienvenida.registro, name='registro'),
    path('login/', home_bienvenida.login, name='login'),
    path('home/', home_views.home, name='home')
]
