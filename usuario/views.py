from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Usuario


def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')

        # Validações
        if password != password_confirm:
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'usuario/cadastro.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe!')
            return render(request, 'usuario/cadastro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado!')
            return render(request, 'usuario/cadastro.html')

        # Criar usuário
        user = User.objects.create_user(username=username, email=email, password=password)
        Usuario.objects.create(user=user, endereco=endereco, telefone=telefone)

        messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
        return redirect('login')

    return render(request, 'usuario/cadastro.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}!')
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')

    return render(request, 'usuario/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')
