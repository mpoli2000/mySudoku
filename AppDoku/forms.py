from django import forms

class Form_Editar_MiJuego(forms.Form):
    nombre = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=200)
    