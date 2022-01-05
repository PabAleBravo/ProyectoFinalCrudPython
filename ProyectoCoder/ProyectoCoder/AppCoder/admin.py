from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from .models import *

admin.site.register(Clientes)

admin.site.register(Proveedores)

admin.site.register(Productos)

admin.site.register(Servicios)
