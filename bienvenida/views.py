from django.shortcuts import render

# Create your views here.
def bienvenida(request):
    return render(request, 'bienvenida.html')

def registro(request):
    return render(request, 'registro.html')

def login(request):
    return render(request, 'login.html')