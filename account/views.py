from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'account/cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/account/cadastro')

        if len(username.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/account/cadastro')

        user = User.objects.filter(username=username)

        # if user.exists():
        if User.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse username')
            return redirect('/account/login')

        try:
            user = User.objects.create_user(username=username,
                                            password=senha)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')

            return render('/account/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/account/cadastro')


def login(request):
    if request.method == "GET":
        return render(request, '/account/login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        usuario = auth.authenticate(username=username, password=senha)
        if not usuario:
            messages.error(request, 'Username ou senha inválidos')
            return redirect('/account/login.html')
        else:
            auth.login(request, usuario)
        return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/account/login.html')