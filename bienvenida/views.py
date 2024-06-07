from django.shortcuts import render, redirect
from django.contrib import messages
from .models import usuarios
from .forms import formularioLogin
from django.contrib.auth import logout

# Create your views here.
def bienvenida(request):
    return render(request, 'bienvenida.html')

def registro(request):
    if request.method == 'POST':
        usuario = request.POST['nombre']
        contraseña = request.POST['contraseña']
        contraseña1 = request.POST['contraseña1']
        email = request.POST['correo']
        
        if contraseña != contraseña1:
            messages.error(request, "Error: Las contraseñas no coinciden.")     
            return redirect('registro')
        
        # Verificar si el nombre de usuario ya existe
        if usuarios.objects.filter(nombre=usuario).exists():
            messages.error(request, "Error: Este nombre de usuario ya está en uso.")
            return redirect('registro')
        
        # Verificar si el correo electrónico ya está en uso
        if usuarios.objects.filter(correo=email).exists():
            messages.error(request, "Error: Este correo electrónico ya está en uso.")
            return redirect('registro')
    
        # Crear un nuevo usuario
        nuevo_usuario = usuarios(nombre=usuario, contraseña=contraseña, correo=email)
        nuevo_usuario.save()
        messages.success(request, "¡Cuenta creada correctamente!")
        return redirect('home')
    else:
        messages.error(request, "Algo paso mal, vuelve a intentar despues!")
        return render(request, 'registro.html')
                
def login(request):
    if request.method == 'POST':
        usuario = request.POST.get('nombre')
        contraseña = request.POST.get('contraseña')
        
        if usuarios.objects.filter(nombre=usuario, contraseña=contraseña):
            messages.success(request, "cuenta logueada exitosamente")
            return redirect('home')
    else: 
        messages.success(request, "Ocurrio algo inesperado, intentalo de nuevo")
        return render(request, 'login.html')
    return render(request, 'login.html')

def cerrarSesion(request):
    logout(request)
    return redirect('bienvenida')