from django.shortcuts import render, redirect
from django.contrib import messages
from .models import usuarios
from .forms import formularioLogin

# Create your views here.
def bienvenida(request):
    return render(request, 'bienvenida.html')

def registro(request):
    if request.method == 'POST':
        usuario = request.POST['nombre']
        contraseña = request.POST['contraseña']
        contraseña1 = request.POST['contraseña1']
        correo = request.POST['correo']
        
        if contraseña != contraseña1:
            messages.error(request, "Error: Las contraseñas no coinciden.")
            return redirect('registro')
        
        # Verificar si el nombre de usuario ya existe
        if usuarios.objects.filter(nombre=usuario).exists():
            messages.error(request, "Error: Este nombre de usuario ya está en uso.")
            return redirect('registro')
        
        # Verificar si el correo electrónico ya está en uso
        if usuarios.objects.filter(correo=correo).exists():
            messages.error(request, "Error: Este correo electrónico ya está en uso.")
            return redirect('registro')
    
        # Crear un nuevo usuario
        nuevo_usuario = usuarios(nombre=usuario, contraseña=contraseña, correo=correo)
        nuevo_usuario.save()
        messages.success(request, "¡Cuenta creada correctamente!")
        return redirect('home')
    else:
        return render(request, 'registro.html')
                
def login(request):
    if request.method == 'GET':
        usuario = request.GET.get('nombre')
        contraseña = request.GET.get('contraseña')
        
        if usuarios.objects.filter(nombre=usuario, contraseña=contraseña):
            messages.success(request, "cuenta logueada exitosamente")
            return redirect('home')
    else: 
        messages.success(request, "Ocurrio algo inesperado, intentalo de nuevo")
        return render(request, 'login.html')
    return render(request, 'login.html')