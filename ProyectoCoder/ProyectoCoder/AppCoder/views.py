from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import detail
from django.views.generic.base import TemplateResponseMixin

from AppCoder.models import Clientes
from AppCoder.models import Proveedores
from AppCoder.models import Productos
from AppCoder.models import Servicios
from AppCoder.forms import ClientesFormulario
from AppCoder.forms import ProveedoresFormulario
from AppCoder.forms import ProductosFormulario
from AppCoder.forms import ServiciosFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.

def inicio(request):
    #return HttpResponse ("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html')

# CREAR REGISTROS
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

def login(request):
    #return HttpResponse ("Esto es una prueba del inicio")
    return render(request, 'AppCoder/login.html')


# LEER REGISTROS------------------------------------------------------------------------------------ 
def leerProductos(request):
    productos = Productos.objects.all()
    prod ={"productos":productos} # contexto
    return render(request, 'AppCoder/leerProductos.html',prod)

def leerServicios(request):
    servicios = Servicios.objects.all()
    serv ={"servicios":servicios} # contexto
    return render(request, 'AppCoder/leerServicios.html',serv)

def leerProveedores(request):
    proveedores = Proveedores.objects.all()
    prov ={"proveedores":proveedores} # contexto
    return render(request, 'AppCoder/leerProveedores.html',prov)

def leerClientes(request):
    clientes = Clientes.objects.all()
    clie ={"clientes":clientes} # contexto
    return render(request, 'AppCoder/leerClientes.html',clie)

# ELIMINAR REGISTROS------------------------------------------------------------------------------------     
def eliminarCliente(request,nombre_para_borrar):
    clienteParaBorrar = Clientes.objects.get(nombre=nombre_para_borrar)
    clienteParaBorrar.delete()

    clientes = Clientes.objects.all()
    return render(request,'AppCoder/leerClientes.html',{"clientes":clientes}) 

def eliminarProducto(request,nombre_para_borrar):
    productoParaBorrar = Productos.objects.get(nombre=nombre_para_borrar)
    productoParaBorrar.delete()

    productos = Productos.objects.all()
    return render(request,'AppCoder/leerProductos.html',{"productos":productos})

def eliminarServicio(request,nombre_para_borrar):
    servicioParaBorrar = Servicios.objects.get(nombre=nombre_para_borrar)
    servicioParaBorrar.delete()

    servicios = Servicios.objects.all()
    return render(request,'AppCoder/leerServicios.html',{"servicios":servicios})

def eliminarProveedor(request,nombre_para_borrar):
    proveedorParaBorrar = Proveedores.objects.get(nombre=nombre_para_borrar)
    proveedorParaBorrar.delete()

    proveedores = Proveedores.objects.all()
    return render(request,'AppCoder/leerProveedores.html',{"proveedores":proveedores})

# MOFIFICAR REGISTROS------------------------------------------------------------------------------------  
def editarProducto(request, nombre_para_editar):
    producto = Productos.objects.get(nombre=nombre_para_editar)
    if request.method == "POST":
        formularioProductos = ProductosFormulario(request.POST)
        if formularioProductos.is_valid():
            informacion = formularioProductos.cleaned_data
            
            producto.nombre=informacion["nombre"]
            producto.modelo=informacion["modelo"]
            producto.marca=informacion["marca"]
                
            producto.save() #Es el que guarda en el DB
            return render(request, 'AppCoder/inicio.html')
    else:
        formularioProductos=ProductosFormulario(initial={"nombre":producto.nombre,"modelo":producto.modelo,"marca":producto.marca})
    return render(request, 'AppCoder/editarProducto.html',{"formularioProductos":formularioProductos,"nombre_para_editar":nombre_para_editar})  

def editarCliente(request, nombre_para_editar):
    cliente = Clientes.objects.get(nombre=nombre_para_editar)
    if request.method == "POST":
        formularioClientes = ClientesFormulario(request.POST)
        if formularioClientes.is_valid():
            informacion = formularioClientes.cleaned_data
            
            cliente.nombre=informacion["nombre"]
            cliente.direccion=informacion["direccion"]
            cliente.telefono=informacion["telefono"]
            cliente.ciudad=informacion["ciudad"]
            cliente.vendedor=informacion["vendedor"]
            cliente.fechaAlta=informacion["fechaAlta"]
                
            cliente.save() #Es el que guarda en el DB
            return render(request, 'AppCoder/inicio.html')
    else:
        formularioClientes=ClientesFormulario(initial={"nombre":cliente.nombre,"direccion":cliente.direccion,"telefono":cliente.telefono,"ciudad":cliente.ciudad,"vendedor":cliente.vendedor,"fechaAlta":cliente.fechaAlta})
    return render(request, 'AppCoder/editarCliente.html',{"formularioClientes":formularioClientes,"nombre_para_editar":nombre_para_editar})


def editarProveedor(request, nombre_para_editar):
    proveedor = Proveedores.objects.get(nombre=nombre_para_editar)
    if request.method == "POST":
        formularioProveedores = ProveedoresFormulario(request.POST)
        if formularioProveedores.is_valid():
            informacion = formularioProveedores.cleaned_data
            
            proveedor.nombre=informacion["nombre"]
            proveedor.direccion=informacion["direccion"]
            proveedor.telefono=informacion["telefono"]
            proveedor.ciudad=informacion["ciudad"]
            proveedor.fechaAlta=informacion["fechaAlta"]
                
            proveedor.save() #Es el que guarda en el DB
            return render(request, 'AppCoder/inicio.html')
    else:
        formularioProveedores=ProveedoresFormulario(initial={"nombre":proveedor.nombre,"direccion":proveedor.direccion,"telefono":proveedor.telefono,"ciudad":proveedor.ciudad,"fechaAlta":proveedor.fechaAlta})
    return render(request, 'AppCoder/editarProveedor.html',{"formularioProveedores":formularioProveedores,"nombre_para_editar":nombre_para_editar})


def editarServicio(request, nombre_para_editar):
    servicio = Servicios.objects.get(nombre=nombre_para_editar)
    if request.method == "POST":
        formularioServicios = ServiciosFormulario(request.POST)
        if formularioServicios.is_valid():
            informacion = formularioServicios.cleaned_data
            
            servicio.nombre=informacion["nombre"]
            servicio.tipoServicio=informacion["tipoServicio"]
            servicio.descripcion=informacion["descripcion"]
                
            servicio.save() #Es el que guarda en el DB
            return render(request, 'AppCoder/inicio.html')
    else:
        formularioServicios=ServiciosFormulario(initial={"nombre":servicio.nombre,"tipoServicio":servicio.tipoServicio,"descripcion":servicio.descripcion})
    return render(request, 'AppCoder/editarServicio.html',{"formularioServicios":formularioServicios,"nombre_para_editar":nombre_para_editar})


# DETALLE DE REGISTROS------------------------------------------------------------------------------------  

#super leer - buscar

class DetalleProducto(DetailView):
    model = Productos
    template_name ="AppCoder/detalleProductos.html"

class DetalleServicio(DetailView):
    model = Servicios
    template_name ="AppCoder/detalleServicios.html"

# LOGIN

def login(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                
                login(request, user)
                return render(request, "AppCoder/inicio.html", {"mensaje":f"BIENVENIDO, {usuario}!!!!"})
                
            else:
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"DATOS MALOS :(!!!!"})
                
            
        else:
            
            return render(request, "AppCoder/inicio.html", {"mensaje":f"FORMULARIO erroneo"})
            
            
    
    
    form = AuthenticationForm()  #Formulario sin nada para hacer el login
    
    return render(request, "AppCoder/login.html", {"form":form} )  