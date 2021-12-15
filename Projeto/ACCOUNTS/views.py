from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)
    # Se caso não existir o usuário cadastrado, retornará None e assim podemos
    # fazer algumas verificações, como segue a baixo

    if not user:
        messages.error(request, 'Usuário ou senha incorreto!')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso.')
        return redirect('contatos')


@login_required(redirect_field_name='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(redirect_field_name='login')
def register_user(request):
    if request.method != 'POST':
        return render(request, 'accounts/register_user.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha \
            or not senha2:
        messages.error(request, 'Nenhum campo pode ficar vázio!')
        return render(request, 'accounts/register_user.html')

    try:
        validate_email(email)
    except Exception:
        messages.error(request, 'Email inválido!')
        return render(request, 'accounts/register_user.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais!')
        return render(request, 'accounts/register_user.html')

    if len(usuario) < 6:
        messages.error(request, 'Uusário precisa ter 6 caracteres ou mais!')
        return render(request, 'accounts/register_user.html')

    if senha != senha2:
        messages.error(request, 'Senhas não conferem!')
        return render(request, 'accounts/register_user.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já cadastrado!')
        return render(request, 'accounts/register_user.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já cadastrado!')
        return render(request, 'accounts/register_user.html')

    messages.success(request, 'Usuário cadastrado com sucesso!\n Faça login.')

    user = User.objects.create_user(first_name=nome, last_name=sobrenome,
                                    email=email, username=usuario,
                                    password=senha)
    user.save()

    return redirect('login')


# Esse decorator obrigada estar logado para acessar a register_contact!
@login_required(redirect_field_name='login')
def register_contact(request):
    if request.method != 'POST':
        form = FormContato()
        return render(
            request,
            'accounts/register_contact.html',
            {'form': form}
            )

    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário!')
        form = FormContato(request.POST)
        return render(
            request,
            'accounts/register_contact.html',
            {'form': form}
            )

    contato = request.POST.get('nome') + request.POST.get('sobrenome')

    form.save()
    messages.success(request, f'Contato {contato} salvo com sucesso!')
    return redirect('register_contact')
