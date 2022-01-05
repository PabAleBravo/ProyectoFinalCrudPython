from django.db import models



# Create your models here.

class Clientes(models.Model):
    nombre =models.CharField(max_length=40)
    direccion =models.CharField(max_length=40)
    telefono =models.IntegerField()
    ciudad =models.CharField(max_length=50)
    vendedor =models.CharField(max_length=40)
    fechaAlta =models.DateField()

    def __str__(self):
        return f"Nombre del Cliente: {self.nombre} Dirección: {self.direccion} Teléfono: {self.telefono} Ciudad: {self.ciudad} Vendedor: {self.vendedor} Fecha de Alta: {self.fechaAlta}"

class Proveedores(models.Model):
    nombre =models.CharField(max_length=40)
    direccion =models.CharField(max_length=40)
    telefono =models.IntegerField()
    ciudad =models.CharField(max_length=40)
    fechaAlta =models.DateField()

    def __str__(self):
        return f"Nombre del Proveedor: {self.nombre} Dirección: {self.direccion} Teléfono: {self.telefono} Ciudad: {self.ciudad} Fecha de Alta: {self.fechaAlta}"
    

class Productos(models.Model):
    nombre =models.CharField(max_length=40)
    modelo =models.CharField(max_length=40)
    marca =models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre del Producto: {self.nombre} Modelo: {self.modelo} Marca: {self.marca}"

class Servicios(models.Model):
    nombre =models.CharField(max_length=40)
    tipoServicio=models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return f"Nombre del Servicio: {self.nombre} Tipo de Servicio: {self.tipoServicio} Descripción: {self.descripcion}"