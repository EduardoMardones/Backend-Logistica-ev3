# transporte/auth_views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def login_view(request):
    """Vista de login HTML"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido {user.first_name or user.username}!')
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'auth/login.html')


@csrf_protect
def register_view(request):
    """Vista de registro HTML"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        # Validaciones
        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'auth/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe')
            return render(request, 'auth/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está registrado')
            return render(request, 'auth/register.html')
        
        # Crear usuario
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error al registrar usuario: {str(e)}')
    
    return render(request, 'auth/register.html')


def logout_view(request):
    """Vista de logout"""
    logout(request)
    messages.success(request, '¡Sesión cerrada exitosamente!')
    return redirect('login')


@login_required
def profile_view(request):
    """Vista de perfil del usuario"""
    return render(request, 'auth/profile.html')