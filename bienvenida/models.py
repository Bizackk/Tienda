from django.db import models

# Create your models here.
class usuarios(models.Model):
    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    
class recepcionistas(models.Model):
    IDrecepcionista = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)