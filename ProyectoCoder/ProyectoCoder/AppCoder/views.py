from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.models import Clientes
from AppCoder.models import Proveedores
from AppCoder.models import Productos
from AppCoder.models import Servicios
from AppCoder.forms import ClientesFormulario
from AppCoder.forms import ProveedoresFormulario
from AppCoder.forms import ProductosFormulario
from AppCoder.forms import ServiciosFormulario





# Create your views here.

def inicio(request):
    #return HttpResponse ("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html')

def proveedores(request):
    formularioProveedores = ClientesFormulario(request.POST)
    if request.method == "POST":
        if formularioProveedores.is_valid():
            informacion = formularioProveedores.cleaned_data
            proveeInst = Proveedores(nombre=informacion["nombre"],direccion=informacion["direccion"],telefono=informacion["telefono"],ciudad=informacion["ciudad"],fechaAlta=informacion["fechaAlta"])
            proveeInst.save() #Es el que guarda en el DB
            return render(request, 'AppCoder/inicio.html')
    else:
        formularioProveedores=ProveedoresFormulario()
    return render(request, 'AppCoder/proveedores.html',{"formularioProveedores":formularioProveedores})
    

def clientes(request):
    formularioClientes = ClientesFormulario(request.POST)
    if request.method == "POST":
        if formularioClientes.is_valid():
            informacion = formularioClientes.cleaned_data
            clientesInst = Clientes(nombre=informacion["nombre"],direccion=informacion["direccion"],telefono=informacion["telefono"],ciudad=informacion["ciudad"],vendedor=informacion["vendedor"],fechaAlta=informacion["fechaAlta"])
            clientesInst.save() #Es el que guarda en el DB
            return render(request, 'AppCoder/inicio.html')
    else:
        formularioClientes=ClientesFormulario()
    return render(request, 'AppCoder/clientes.html',{"formularioClientes":formularioClientes})

def servicios(request):
    formularioServicios = ServiciosFormulario(request.POST)
    if request.method == "POST":
        if formularioServicios.is_valid():
            informacion = formularioServicios.cleaned_data
            servInst = Servicios(nombre=informacion["nombre"],tipoServicio=informacion["tipoServicio"],descripcion=informacion["descripcion"])
            servInst.save() #Es el que guarda en el DB
            return render(request, 'AppCoder/inicio.html')
    else:
        formularioServicios=ServiciosFormulario()
    return render(request, 'AppCoder/servicios.html',{"formularioServicios":formularioServicios})

def productos(request):
    formularioProductos = ProductosFormulario(request.POST)
    if request.method == "POST":
        if formularioProductos.is_valid():
            informacion = formularioProductos.cleaned_data
            producInst = Productos(nombre=informacion["nombre"],modelo=informacion["modelo"],marca=informacion["marca"])
            producInst.save() #Es el que guarda en el DB
            return render(request, 'AppCoder/inicio.html')
    else:
        formularioProductos=ProductosFormulario()
    return render(request, 'AppCoder/productos.html',{"formularioProductos":formularioProductos})

def contacto(request):
    #return HttpResponse ("Esto es una prueba del inicio")
    return render(request, 'AppCoder/contacto.html')
