from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='contatos'),
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
    # <> significa que iremos passar argumentos para a nossa função dentro da
    # nossa view, aí coloca o tipo dele e o nome dele.
    path('busca/', views.busca, name='busca'),

]
