from django import forms

class formularioLogin(forms.Form):
    nombre = forms.CharField()
    contraseña = forms.IntegerField()