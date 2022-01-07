from django import forms


from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields


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


class UserRegisterForm(UserCreationForm):

    #Obligatorios
    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    #Extra
    last_name = forms.CharField()
    first_name = forms.CharField()
   
    #imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 


#Formulario edicion perfil
class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Ingrese su email")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 