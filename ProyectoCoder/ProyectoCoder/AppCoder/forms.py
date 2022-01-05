from django import forms
from django.forms.forms import Form

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClientesFormulario(forms.Form):
    nombre =forms.CharField(max_length=40)
    direccion =forms.CharField(max_length=40)
    telefono =forms.IntegerField()
    ciudad =forms.CharField(max_length=50)
    vendedor =forms.CharField(max_length=40)
    fechaAlta =forms.DateField()

class ProveedoresFormulario(forms.Form):
    nombre =forms.CharField(max_length=40)
    direccion =forms.CharField(max_length=40)
    telefono =forms.IntegerField()
    ciudad =forms.CharField(max_length=40)
    fechaAlta =forms.DateField()

class ProductosFormulario(forms.Form):
    nombre =forms.CharField(max_length=40)
    modelo =forms.CharField(max_length=40)
    marca =forms.CharField(max_length=40)

class ServiciosFormulario(forms.Form):
    nombre =forms.CharField(max_length=40)
    tipoServicio=forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=500)


