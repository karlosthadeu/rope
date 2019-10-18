from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rope.settings import MEDIA_URL

# Models
from .models import Publicacao as PublicacaoModel
from .models import Materia as MateriaModel
from .models import PlanoDeEstudo as PlanoDeEstudoModel

#Forms
from .forms import PublicacoesForm
from .forms import MateriaForm
from .forms import PlanoDeEstudoForm

#Constantes de roteamento
PRINCIPAL = r'principal'
MATERIAS = r'materias'
EM_CONSTRUCAO = r'em_construcao'
PLANOS_DE_ESTUDO = r'planos_de_estudo'
PUBLICACOES = r'publicacoes'

# Create your views here.
class PrincipalView():
    @staticmethod
    def inicio(request):
        publicacoes_mais_recentes = PublicacaoModel.objects.all();

        dados = {
            'titulo': 'Página inicial',
            'publicacoes_mais_recentes': publicacoes_mais_recentes,
            'MEDIA_URL': MEDIA_URL,
        }

        return render(request, PRINCIPAL+'/inicio.html', dados)

    @staticmethod
    def pagina_em_construcao(request):
        return render(request, PRINCIPAL+'/em_construcao.html')

class ChamadosView():
    @staticmethod
    def criar(request):
        return redirect(EM_CONSTRUCAO)

    @staticmethod
    def fechar(request, id):
        return redirect(EM_CONSTRUCAO)

    @staticmethod
    def responder(request, id):
        return redirect(EM_CONSTRUCAO)

    @staticmethod
    def avaliar(request, id):
        return redirect(EM_CONSTRUCAO)

class HistoricosView():
    pass

class MateriasView():
    """
        Gerenciamento de matérias.
    """
    @staticmethod
    @login_required(redirect_field_name='entrar')
    def modificar(request, id):
        """
        Modificar matéria.
        """
        materia = get_object_or_404(MateriaModel, pk=id)
        form = MateriaForm(request.POST or None, instance=materia)

        if form.is_valid():
            form.save()
            return HttpResponse('Deu certo') # Alterar essa linha para redirecionar para uma página específica.
        else:
            dados = {
                'titulo': 'Modificar Matéria',
                'form': form,
                'materia': materia
            }

            return render(request, MATERIAS+'/modificar.html', dados)

    @staticmethod
    @login_required(redirect_field_name='entrar')
    def criar(request):
        """
        Criar matérias.
        Permissão: Administradores e super usuários.
        """
        form = MateriaForm(request.POST or None)
        

        if form.is_valid():
            form.save()
            return HttpResponse('Deu certo') # Alterar essa linha para redirecionar para uma página específica.
        else:
            dados = {
                'titulo': 'Criar Matéria',
                'form': form
            }

            return render(request, 'materias/criar.html', dados)

    @staticmethod
    @login_required(redirect_field_name='entrar')
    def listar_por_area_de_conhecimento(request, area_conhecimento):
        materias = MateriaModel.objects.filter(area_de_conhecimento = area_conhecimento).order_by('-id')

        dados = {
            'titulo': f'Listagem de Matérias: {area_conhecimento}',
            'materias': materias
        }

        return render(request, 'materias/listar_por_area_conhecimento.html', dados)

class PlanosDeEstudosView():
    """
        Gerenciamento do plano de estudo
    """

    @staticmethod
    @login_required(redirect_field_name='entrar')
    def criar(request):
        """
            Cria uma plano de estudo 
        """
        
        form = PlanoDeEstudoForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('')
        else:
            dados = {
                'titulo': 'Criar Plano De Estudo',
                'form': form
            }

            return render(request, PLANOS_DE_ESTUDO+'/criar.html', dados)

    @staticmethod
    @login_required(redirect_field_name='entrar')
    def modificar(request, id):
        """
            Modifica o plano de estudo
        """
        
        plano = get_object_or_404(PlanoDeEstudoModel, pk=id)
        form = MateriaForm(request.POST or None, instance=plano)

        if form.is_valid():
            form.save()
            return redirect('')
        else:
            dados = {
                'titulo': 'Modificar Plano De Estudo',
                'form': form,
                'materia': plano
            }

            return render(request, PLANOS_DE_ESTUDO+'/modificar.html', dados)

    @staticmethod
    @login_required(redirect_field_name='entrar')
    def apagar_publicacao(request, id):
        """
            Apaga uma publicação do plano de estudo
        """
        
        #retorna true caso excluir e false caso não
        if PlanoDeEstudoModel.objects.delete(pk=id) :
            return HttpResponse('ok') 
        else :
            return HttpResponse('Não deu certo')
        
    @staticmethod
    @login_required(redirect_field_name='entrar')
    def adicionar_publicacao(request, id):
        """
            Adiciona uma publicação ao plano de estudo
        """
        
        status = PlanoDeEstudoModel.object.save(id)

        return render(request, PLANOS_DE_ESTUDO+'/adicionar_publicacao.html', status)

    @staticmethod
    def listar(request):
        """
            Lista os planos de estudos existentes
        """
        
        planos_de_estudo = list(PlanoDeEstudoModel.object.all())

        return render(request, PLANOS_DE_ESTUDO+'/listar.html')

    @staticmethod
    def visualizar(request, id):
        """
            Visualizar o plano de estudo por completo 
        """
        
        plano_de_estudo = PlanoDeEstudoModel.object.all().filter(id=id)

        return render(request, PLANOS_DE_ESTUDO+'/visualizar', plano_de_estudo)

class PublicacoesView():
    # Na primeira verificação tá ok
    @staticmethod
    @login_required(redirect_field_name='entrar')
    def listar(request):
        publicacoes = PublicacaoModel.objects.all()
        
        dados = {
            'titulo': 'Listar Publicações',
            'publicacoes': publicacoes 
        }

        return render(request, PUBLICACOES+'/listar.html', dados)
    
    # Na primeira verificação tá ok
    @staticmethod
    @login_required(redirect_field_name='entrar')
    def criar(request):
        form = PublicacoesForm(request.POST or None)

        if form.is_valid() :
            publicacao = form.save()
            publicacao.usuario = request.user
            publicacao.save()

            return redirect('publicacoes_listar')

        else:
            dados = {
                'titulo': 'Criar Publicação',
                'form': form,
            }

            return render(request, PUBLICACOES+'/criar.html', dados)
    
    # Na primeira verificação tá ok
    @staticmethod
    @login_required(redirect_field_name='entrar')
    def modificar(request, id):
        publicacao = get_object_or_404(PublicacaoModel, pk=id)
        form = PublicacoesForm(request.POST or None, instance=publicacao)

        if form.is_valid():
            form.save()
            return redirect('publicacoes_listar')
        
        else:
            dados = {
                'titulo': 'Modificar Publicação',
                'form': form,
                'publicacao': publicacao,
            }

            return render(request, PUBLICACOES+'/modificar.html', dados)

    @staticmethod
    @login_required(redirect_field_name='entrar')
    def visualizar(request, id):
        return HttpResponse('Visualizar publicação')
    
    @staticmethod
    @login_required(redirect_field_name='entrar')
    def apagar(request, id):
        publicacao = get_object_or_404(PublicacaoModel, pk=id)
        publicacao.delete()

        return redirect('publicacoes_listar')

    @staticmethod
    @login_required(redirect_field_name='entrar')
    def listar_por_materia(request, materia_id):
        """
        Listar publicações com base em uma materia específica.
        """
        materia = get_object_or_404(MateriaModel, pk=materia_id)
        publicacoes = PublicacaoModel.objects.filter(materia = materia_id).order_by('-id')

        dados = {
            'titulo': 'Listar Publicações por matéria',
            'publicacoes': publicacoes,
        }

        return render(request, PUBLICACOES+'/listar_por_materia.html', dados)