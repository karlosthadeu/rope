from django.urls import path
from .views import PublicacoesView, PrincipalView, ChamadosView, PlanosDeEstudosView

"""
    Em paths especiais, como os de modificação e apagar, tem que ser verificado se o usuário que está
    fazendo isso é o "dono"

    Em "publicação", fora listar e visualizar, as outras ações têm que passar por verificação se é um 
    professor que está tentando acessar esse requisito

"""


urlpatterns = [
    path('',                                        PrincipalView.inicio,               name='inicio'),
    path('em_construcao',                           PrincipalView.pagina_em_construcao, name='em_construcao'),

    # Publicações:
    path('publicacoes/listar',                      PublicacoesView.listar,         name='publicacoes_listar'),
    path('publicacoes/criar',                       PublicacoesView.criar,          name='publicacoes_criar'),
    path('publicacoes/modificar/<str:id>',          PublicacoesView.modificar,      name='publicacoes_modificar'),
    path('publicacoes/visualizar/<str:id>',         PublicacoesView.visualizar,     name='publicacoes_visualizar'),
    path('publicacoes/apagar/<str:id>',             PublicacoesView.apagar,         name='publicacoes_apagar'),

    # Planos de estudo:
    path('planos_de_estudo/criar',                  PlanosDeEstudosView.criar,                  name='planos_de_estudo_criar'),
    path('planos_de_estudo/modificar',              PlanosDeEstudosView.modificar,              name='planos_de_estudo_modificar'),
    path('planos_de_estudo/apagar_publicacao',      PlanosDeEstudosView.apagar_publicacao,      name='planos_de_estudo_apagar_publicacao'),
    path('planos_de_estudo/adicionar_publicacao',   PlanosDeEstudosView.adicionar_publicacao,   name='planos_de_estudo_criar'),
    path('planos_de_estudo/listar',                 PlanosDeEstudosView.listar,                 name='listar'),
    path('planos_de_estudo/visualizar',             PlanosDeEstudosView.visualizar,             name='visualizar'),

    # Chamados:
    path('chamados/criar',                      ChamadosView.criar,             name='chamados_criar'),
    path('chamados/responder/<int:id>',         ChamadosView.responder,         name='chamados_responder'),
    path('chamados/fechar/<int:id>',            ChamadosView.fechar,            name='chamados_fechar'),
    path('chamados/avaliar/<int:id>',           ChamadosView.avaliar,           name='chamados_avaliar'),
]