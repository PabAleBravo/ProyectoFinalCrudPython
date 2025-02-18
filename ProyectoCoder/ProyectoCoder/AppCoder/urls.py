from django.urls import path
from AppCoder import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio',views.inicio, name="Inicio"),
    path('proveedores',views.proveedores, name="Proveedores"),
    path('clientes',views.clientes, name="Clientes"),
    path('servicios',views.servicios, name="Servicios"),
    path('productos',views.productos, name="Productos"),
    path('contacto',views.contacto, name="Contacto"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),


    path('leerProductos',views.leerProductos, name="LeerProductos"),
    path('leerServicios',views.leerServicios, name="LeerServicios"),
    path('leerProveedores',views.leerProveedores, name="LeerProveedores"),
    path('leerClientes',views.leerClientes, name="LeerClientes"),
    
    path('eliminarCliente/<nombre_para_borrar>/',views.eliminarCliente, name="EliminarCliente"),
    path('eliminarProducto/<nombre_para_borrar>/',views.eliminarProducto, name="EliminarProducto"),
    path('eliminarServicio/<nombre_para_borrar>/',views.eliminarServicio, name="EliminarServicio"),
    path('eliminarProveedor/<nombre_para_borrar>/',views.eliminarProveedor, name="EliminarProveedor"),
    
    path('editarProducto/<nombre_para_editar>/',views.editarProducto, name="EditarProducto"),
    path('editarCliente/<nombre_para_editar>/',views.editarCliente, name="EditarCliente"),
    path('editarProveedor/<nombre_para_editar>/',views.editarProveedor, name="EditarProveedor"),
    path('editarServicio/<nombre_para_editar>/',views.editarServicio, name="EditarServicio"),

    #URL PARA CLASES BASADAS EN VITAS
    path(r'^(?P<pk>\d+)$',views.DetalleProducto.as_view(), name='DetalleProducto'),
    path(r'detalleServicio(?P<pk>\d+)$',views.DetalleServicio.as_view(), name='DetalleServicio'),
    path(r'detalleProveedor(?P<pk>\d+)$',views.DetalleProveedor.as_view(), name='DetalleProveedor'),
    path(r'detalleCliente(?P<pk>\d+)$',views.DetalleCliente.as_view(), name='DetalleCliente'),

    #BUSCAR
    path('buscarproducto/',views.buscarproducto, name="buscarproducto"),
    path('buscarservicio/',views.buscarservicio, name="buscarservicio"),
    path('buscarproveedor/',views.buscarproveedor, name="buscarproveedor"),
    path('buscarcliente/',views.buscarcliente, name="buscarcliente"),



    
]