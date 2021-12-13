from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.models import Clientes

from AppCoder.forms import ClientesFormulario


# Create your views here.

def inicio(request):
    #return HttpResponse ("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html')

def proveedores(request):
    #return HttpResponse ("Esto es una prueba del inicio")
    return render(request, 'AppCoder/proveedores.html')
    

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
    #return HttpResponse ("Esto es una prueba del inicio")
    return render(request, 'AppCoder/servicios.html')

def productos(request):
    #return HttpResponse ("Esto es una prueba del inicio")
    return render(request, 'AppCoder/productos.html')

def contacto(request):
    #return HttpResponse ("Esto es una prueba del inicio")
    return render(request, 'AppCoder/contacto.html')
