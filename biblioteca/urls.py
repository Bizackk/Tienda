from django.contrib import admin
from django.urls import path, include
from bienvenida import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bienvenida.urls')),
    path('home/', include('home.urls')),
]
