from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import detail
from django.views.generic.base import TemplateResponseMixin

from AppCoder.models import Clientes, Proveedores, Productos, Servicios
from AppCoder.forms import ClientesFormulario, ProveedoresFormulario, ProductosFormulario, ServiciosFormulario, UserRegisterForm, UserEditForm


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.models import User


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as dj_login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required




# Create your views here.

def inicio(request):
    #return HttpResponse ("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html')

# CREAR REGISTROS
@login_required
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
    
@login_required
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

@login_required
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

@login_required
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

@login_required
def leerProveedores(request):
    proveedores = Proveedores.objects.all()
    prov ={"proveedores":proveedores} # contexto
    return render(request, 'AppCoder/leerProveedores.html',prov)

@login_required
def leerClientes(request):
    clientes = Clientes.objects.all()
    clie ={"clientes":clientes} # contexto
    return render(request, 'AppCoder/leerClientes.html',clie)

# ELIMINAR REGISTROS------------------------------------------------------------------------------------     
@login_required
def eliminarCliente(request,nombre_para_borrar):
    clienteParaBorrar = Clientes.objects.get(nombre=nombre_para_borrar)
    clienteParaBorrar.delete()

    clientes = Clientes.objects.all()
    return render(request,'AppCoder/leerClientes.html',{"clientes":clientes}) 

@login_required
def eliminarProducto(request,nombre_para_borrar):
    productoParaBorrar = Productos.objects.get(nombre=nombre_para_borrar)
    productoParaBorrar.delete()

    productos = Productos.objects.all()
    return render(request,'AppCoder/leerProductos.html',{"productos":productos})

@login_required
def eliminarServicio(request,nombre_para_borrar):
    servicioParaBorrar = Servicios.objects.get(nombre=nombre_para_borrar)
    servicioParaBorrar.delete()

    servicios = Servicios.objects.all()
    return render(request,'AppCoder/leerServicios.html',{"servicios":servicios})

@login_required
def eliminarProveedor(request,nombre_para_borrar):
    proveedorParaBorrar = Proveedores.objects.get(nombre=nombre_para_borrar)
    proveedorParaBorrar.delete()

    proveedores = Proveedores.objects.all()
    return render(request,'AppCoder/leerProveedores.html',{"proveedores":proveedores})

# MOFIFICAR REGISTROS------------------------------------------------------------------------------------  

@login_required
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

@login_required
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

@login_required
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

@login_required
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
    template_name ="AppCoder/detalleServicio.html"

class DetalleProveedor(DetailView):
    model = Proveedores
    template_name ="AppCoder/detalleProveedor.html"

class DetalleCliente(DetailView):
    model = Clientes
    template_name ="AppCoder/detalleCliente.html"

# LOGIN

def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                
                dj_login(request, user)
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"¡BIENVENIDO, Hola {usuario}! Ahora podes ver todas las funcionalidades."})
                
            else:
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"DATOS incorrectos :(!!!!"})
                
            
        else:
            
            return render(request, "AppCoder/inicio.html", {"mensaje":f"FORMULARIO erroneo"})
            
            
    
    
    form = AuthenticationForm()  #Formulario sin nada para hacer el login
    
    return render(request, "AppCoder/login.html", {"form":form} )


    # REGISTRO DE USUARIO

def register(request):
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
            
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/inicio.html" ,  {"mensaje":f" Usuario {username} Creado"})


    else:
       
              
        form = UserRegisterForm()     

    return render(request,"AppCoder/register.html" ,  {"form":form})


# EDITAR USUARIO

@login_required
def editarPerfil(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data

            usuario.set_password(informacion.get('password1'))
            usuario.save()
            update_session_auth_hash(request, usuario)


            return render(request, "AppCoder/inicio.html",{f"mensaje":f"Se guardó con Exito"})
        
    else:
        
        miFormulario = UserEditForm(initial={'email':usuario.email})
        
        
    return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

#BUSCAR----------------------------------------------------------------------------------------------------

def buscarproducto(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        nombre = Productos.objects.filter(marca__icontains=marca)

        return render(request, "AppCoder/resutadobuscarproducto.html", {"marca":marca, "nombre":nombre})
    
    else:
        respuesta = "No se encontro información"

    return HttpResponse(respuesta)

def buscarservicio(request):
    if request.GET["tipoServicio"]:
        tipoServicio = request.GET["tipoServicio"]
        nombre = Servicios.objects.filter(tipoServicio__icontains=tipoServicio)

        return render(request, "AppCoder/resutadobuscarservicio.html", {"tipoServicio":tipoServicio, "nombre":nombre})
    
    else:
        respuesta = "No se encontro información"

    return HttpResponse(respuesta)

def buscarproveedor(request):
    if request.GET["ciudad"]:
        ciudad = request.GET["ciudad"]
        nombre = Proveedores.objects.filter(ciudad__icontains=ciudad)

        return render(request, "AppCoder/resutadobuscarproveedor.html", {"ciudad":ciudad, "nombre":nombre})
    
    else:
        respuesta = "No se encontro información"

    return HttpResponse(respuesta)

def buscarcliente(request):
    if request.GET["ciudad"]:
        ciudad = request.GET["ciudad"]
        nombre = Clientes.objects.filter(ciudad__icontains=ciudad)

        return render(request, "AppCoder/resutadobuscarcliente.html", {"ciudad":ciudad, "nombre":nombre})
    
    else:
        respuesta = "No se encontro información"

    return HttpResponse(respuesta)