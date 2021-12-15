from django.contrib import admin
from .models import Categoria, Contato
# .models é a pasta models dentro de contatos.

# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data_cadastro', 'categoria', 'mostrar')
    # Isso é os atributos a serem exibidos no display do site admin do django.

    list_display_links = ('id', 'nome', 'sobrenome')
    # São os atributos que serão como links para abrir a tela para editar!

    list_filter = ('nome', 'sobrenome')
    # Esse irá criar uma tela de filtro por nome e sobrenome.

    list_per_page = 10
    # Quantidade de Contatos que serão exibidos por página.

    search_fields = ('nome', 'sobrenome', 'telefone')
    # Campos que poderão ser pesquisados
    list_editable = ('telefone', 'mostrar')
    # Faz com que os campos sejam editaveis na tela que aparece todos os
    # contatos, sem precisar clicar no contato para editar!

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    # Isso é os atributos a serem exibidos no display do site admin do django.

    list_display_links = ('id', 'nome')
    # São os atributos que serão como links para abrir a tela para editar!

    list_filter = ('id', 'nome')
    # Esse irá criar uma tela de filtro por nome e sobrenome.

    list_per_page = 10
    # Quantidade de Contatos que serão exibidos por página.

    search_fields = ('id', 'nome')
    # Campos que poderão ser pesquisados


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Contato, ContatoAdmin)
