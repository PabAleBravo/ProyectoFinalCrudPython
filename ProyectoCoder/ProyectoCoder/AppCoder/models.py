from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre =models.CharField(max_length=40)
    direccion =models.CharField(max_length=40)
    telefono =models.IntegerField()
    ciudad =models.CharField(max_length=50)
    vendedor =models.CharField(max_length=40)
    fechaAlta =models.DateField()

class Proveedores(models.Model):
    nombre =models.CharField(max_length=40)
    direccion =models.CharField(max_length=40)
    telefono =models.IntegerField()
    ciudad =models.CharField(max_length=40)
    fechaAlta =models.DateField()
    

class Productos(models.Model):
    nombre =models.CharField(max_length=40)
    modelo =models.CharField(max_length=40)
    marca =models.CharField(max_length=40)