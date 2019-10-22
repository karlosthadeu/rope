from django.urls import path
from .views import PublicacoesView, PrincipalView, ChamadosView, PlanosDeEstudosView, MateriasView

"""
    Em paths especiais, como os de modificação e apagar, tem que ser verificado se o usuário que está
    fazendo isso é o "dono"

    Em "publicação", fora listar e visualizar, as outras ações têm que passar por verificação se é um 
    professor que está tentando acessar esse requisito

"""

#importando os diretórios 
from . import diretorios

urlpatterns = [
    path('',                                                       PrincipalView.inicio,               name='inicio'),
    path(diretorios.EM_CONSTRUCAO,                           PrincipalView.pagina_em_construcao, name='em_construcao'),

    # Publicações:
    path(diretorios.PUBLICACOES+'/listar',                      PublicacoesView.listar,         name='publicacoes_listar'),
    path(diretorios.PUBLICACOES+'/criar',                       PublicacoesView.criar,          name='publicacoes_criar'),
    path(diretorios.PUBLICACOES+'/modificar/<str:id>',          PublicacoesView.modificar,      name='publicacoes_modificar'),
    path(diretorios.PUBLICACOES+'/visualizar/<str:id>',         PublicacoesView.visualizar,     name='publicacoes_visualizar'),
    path(diretorios.PUBLICACOES+'/apagar/<str:id>',             PublicacoesView.apagar,         name='publicacoes_apagar'),
    # Listagem de publicação por matéria:
    path(diretorios.PUBLICACOES+'/listar/materias/<str:materia_id>', PublicacoesView.listar_por_materia, name='publicacoes_listar_por_materia'),

    # Planos de estudo:
    path(diretorios.PLANOS_DE_ESTUDO+'/criar',                  PlanosDeEstudosView.criar,                  name='planos_de_estudo_criar'),
    path(diretorios.PLANOS_DE_ESTUDO+'/modificar/<str:id>',              PlanosDeEstudosView.modificar,              name='planos_de_estudo_modificar'),
    path(diretorios.PLANOS_DE_ESTUDO+'/apagar_publicacao',      PlanosDeEstudosView.apagar_publicacao,      name='planos_de_estudo_apagar_publicacao'),
    path(diretorios.PLANOS_DE_ESTUDO+'/adicionar_publicacao',   PlanosDeEstudosView.adicionar_publicacao,   name='planos_de_estudo_criar'),
    path(diretorios.PLANOS_DE_ESTUDO+'/listar',                 PlanosDeEstudosView.listar,                 name='listar'),
    path(diretorios.PLANOS_DE_ESTUDO+'/visualizar',             PlanosDeEstudosView.visualizar,             name='visualizar'),

    # Chamados:
    path(diretorios.CHAMADOS+'/criar',                      ChamadosView.criar,             name='chamados_criar'),
    path(diretorios.CHAMADOS+'/responder/<int:id>',         ChamadosView.responder,         name='chamados_responder'),
    path(diretorios.CHAMADOS+'/fechar/<int:id>',            ChamadosView.fechar,            name='chamados_fechar'),
    path(diretorios.CHAMADOS+'/avaliar/<int:id>',           ChamadosView.avaliar,           name='chamados_avaliar'),

    # Materias:
    path(diretorios.MATERIAS+'/modificar/<str:id>',         MateriasView.modificar,         name='materias_modificar'),
    path(diretorios.MATERIAS+'/criar',                      MateriasView.criar,             name='materias_criar'),
    path(diretorios.MATERIAS+'/listar/area_conhecimento/<str:area_conhecimento>',                      MateriasView.listar_por_area_de_conhecimento,             name='materias_criar')
]