from django import forms

class ClientesFormulario(forms.Form):
    nombre =forms.CharField(max_length=40)
    direccion =forms.CharField(max_length=40)
    telefono =forms.IntegerField()
    ciudad =forms.CharField(max_length=50)
    vendedor =forms.CharField(max_length=40)
    fechaAlta =forms.DateField()


