#setting.url
from django.contrib import admin
from django.urls import path, include
from bienvenida import views
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', include('bienvenida.urls')),
    path('home/', include('home.urls')),
    path('', RedirectView.as_view(url='bienvenida/', permanent=False)),

]
