#home.urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detalle/<int:game_id>/', views.detalle_juego, name='detalle_juego'),
]
