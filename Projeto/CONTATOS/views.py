from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# O Q, Value e Concat são para as querys SQL complexas


@login_required(redirect_field_name='login')
def index(request):
    # contatos = Contato.objects.all()
    contatos = Contato.objects.order_by('id').filter(
        mostrar=True
    )
    # Usa o order_by para ordernar os dados. Se usar um sinal de menos (-)
    # na frente, ele inverte a ordenação!
    # Fez um filtro, só irá mostrar aqueles que forem Verdadeiros, se caso
    # colocar False, irá mostrar só os que estão como falsos

    '''
    .objects.all() pega todas as instâncias de Contato, ou melhor, todos
    os objetos.
    É como se tivessemos feito um select * from Contato.
    '''

    paginator = Paginator(contatos, 5)
    # Passamos como parâmetro para o Paginator a lista de contatos
    # e a qunatidade que queremos que apareça por página!

    page = request.GET.get('p')
    # Capturamos a página atual no HTML
    contatos = paginator.get_page(page)
    # Renomeamos contatos somente com os 5 contatos na página capturada
    # do HTML

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })
    '''
    Dentro da chave é um dicionário que passamos para o link, no caso,
    aqui é para o nosso index.html!
    Lá dentro do index conseguimos acessar aos dados dos contatos.
    '''


@login_required(redirect_field_name='login')
def ver_contato(request, contato_id):
    # try:
    #     contato = Contato.objects.get(id=contato_id)
    #     return render(request, 'contatos/ver_contato.html', {
    #         'contato': contato
    #     })
    # except Contato.DoesNotExist:
    #     raise Http404()
    # Levantamento de exceção clássico!
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()
    # Se caso for tentar acessar os dados de um contato por ID e mostrar
    # for falso, irá retornar um erro 404, não encontrado!

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato})
    # usando a função get_object_or_404, se caso o objeto não existir ele
    # levanta o erro 404, que não foi encontrado!


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or termo == '':
        messages.add_message(
            request,
            messages.ERROR,
            'Campo pesquisa não pode ficar em branco!'
            )
        return redirect('contatos')
    '''
        o add_message, recebe 1º request, 2º o tipo de mensangem (sucess, error
        warning, debug, info) e depois a mensagem a ser adicionada.
        A função redirect rediciona para uma página, o parâmetro passado a ela
        é o nome da página definido no modulo urls.py do app.
    '''
    campos = Concat('nome', Value(' '), 'sobrenome')
    # Value vazio, representa apenas um espaço no meio a ser concatenado.

    contatos = Contato.objects.annotate(
        nome_completo=campos
        ).filter(
            Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
            )
    '''O annotate é uma função que aceita fazer agragações SQL
    e aceita declarações de váriaveis que seram temporaveis no DB.
    __contains depois da váriavel significa contém, ou seja,
    no filter está dizendo, que nome_completo contém igual ao termo.
    O Q pega uma expressão e aceita fazer OR com o traço vertical (|).
    '''

    paginator = Paginator(contatos, 5)
    # Paginator recebe a lista de contatos e a quantidade que
    # será exibida por página!
    page = request.GET.get('p')
    # Pega a página atual no HTML
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
