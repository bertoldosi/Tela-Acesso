from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from app.entidades.usuario import Usuario
from app.forms import *
from app.services import usuario_service


def Index(request):
    return render(request, 'index.html', locals())

def logar_user(request):
    form_login = LoginForm()
    if request.method == 'POST':
        form_login = LoginForm(data=request.POST)

        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = LoginForm()
    else:
        form_login = LoginForm()
    return render(request, 'logar.html', locals())




def cadastrar_usuario(request):
    form_usuario = UsuarioForm()
    if request.method == 'POST':
        form_usuario = UsuarioForm(data=request.POST)
        if form_usuario.is_valid():

            nome = form_usuario.cleaned_data['nome']
            email = form_usuario.cleaned_data['email']
            password = form_usuario.cleaned_data['password1']

            usuario_novo = Usuario(nome=nome, email=email, password=password)

            usuario_service.cadastrar_usuario(usuario_novo)

            return redirect('logar')
    else:
        form_usuario = UsuarioForm()
    return render(request, 'cadastrar.html', locals())
