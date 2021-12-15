from django.db import models
from django.utils import timezone

"""
CONTATOS
id: INT (automático)
nome: STR * (obrigatório)
sobrenome: STR (opcional)
telefone: STR * (obrigatório)
e-mail: STR (opcional)
data_cadastro: DATETIME * (automático)
descricao: TEXTO (opcional)
categoria: CATEGORIA (outro model)

CATEGORIA
id: INT (automático)
nome: STR * (obrigatório)

OBS: Qualquer alteração que fazer no model aqui
precisa dar os comandos python manage.py makemigrations e o migrate!
"""


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self,):
        return self.nome
        '''
        Esse metodo, muda a maneira de exibir o nosso objeto.
        O que fizemos foi que no lugar de aparecer Object(1) irá aparecer o
        nome da categoria instaciada! No site admin
        '''


class Contato(models.Model):
    # Obrigatório herdar da class Model
    nome = models.CharField(max_length=255)
    # Tipo da váriavel, max_lenght é tamanho máximo
    sobrenome = models.CharField(max_length=255, blank=True)
    # Blank faz o atributo ser opcional.
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    '''default é um parâmetro de padrão de data. O timezone
    importamos ele de django.utils e pegamos a função now que
    pega a data e horário do computador.
    '''
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    ''' ForeignKey faz a relação dos models, o primeiro parâmetro que
    passa é o models a ser ligado. O on_delete é o que deve ser feito
    quando uma categoria for deletado, no caso aqui, falamos para
    fazer nada (models.DO_NOTHING).
    '''
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')
    '''No upload_to, estamos passando o caminho que deverá ser upada as fotos
    teremos uma pasta chamada fotos e dentro dela tera o respectivo ano (%Y)
    que a imagem foi criada, seu respectivo mês (%m) e o respectivo dia também
    (%d) de criação.
    '''

    def __str__(self,):
        return self.nome
