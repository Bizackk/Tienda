from django.db import models

# Create your models here.
class usuario(models.Model):
    IDusuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=9)
    correo = models.EmailField()
    
class recepcionistas(models.Model):
    IDrecepcionista = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    contraseña = models.IntegerField()
    correo = models.EmailField()