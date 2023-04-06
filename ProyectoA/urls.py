from django.contrib import admin
from django.urls import path
from ProyectoA.views import inicio
from ProyectoA.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('home/', home),
]
