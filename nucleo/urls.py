from django.urls import path
from .views import PublicacoesView, PrincipalView

urlpatterns = [
    path('', PrincipalView.inicio, name='principal_view_inicio'),

    # Publicações
    path('publicacoes/listar',                  PublicacoesView.listar,         name='publicacoes_listar'),
    path('publicacoes/criar',                   PublicacoesView.criar,          name='publicacoes_criar'),
    path('publicacoes/modificar/<str:id>',      PublicacoesView.modificar,      name='publicacoes_modificar'),
    path('publicacoes/visualizar/<str:id>',     PublicacoesView.visualizar,     name='publicacoes_visualizar'),
    path('publicacoes/apagar/<str:id>',         PublicacoesView.apagar,         name='publicacoes_apagar'),
]