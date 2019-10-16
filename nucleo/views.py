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

        return render(request, 'principal/inicio.html', dados)

    @staticmethod
    def pagina_em_construcao(request):
        return render(request, 'principal/em_construcao.html')

class ChamadosView():
    @staticmethod
    def criar(request):
        return redirect('em_construcao')

    @staticmethod
    def fechar(request, id):
        return redirect('em_construcao')

    @staticmethod
    def responder(request, id):
        return redirect('em_construcao')

    @staticmethod
    def avaliar(request, id):
        return redirect('em_construcao')

class HistoricosView():
    pass

class MateriaisView():
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
            return redirect('')
        else:
            dados = {
                'titulo': 'Modificar Matéria',
                'form': form,
                'materia': materia
            }

            return render(request, 'materias/modificar.html', dados)

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
            return redirect('')
        else:
            dados = {
                'titulo': 'Criar Matéria',
                'form': form
            }

            return render(request, 'materias/criar.html', dados)

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

            return render(request, 'plano_de_estudo/criar.html', dados)

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

            return render(request, 'plano_de_estudo/modificar.html', dados)

    @staticmethod
    @login_required(redirect_field_name='entrar')
    def apagar_publicacao(request, id):
        """
            Apaga uma publicação do plano de estudo
        """
        return redirect('em_construcao')

    @staticmethod
    @login_required(redirect_field_name='entrar')
    def adicionar_publicacao(request, id):
        """
            Adiciona uma publicação ao plano de estudo
        """
        pass

    @staticmethod
    def listar():
        """
            Lista os planos de estudos existentes
        """
        pass

    @staticmethod
    def visualizar(request, id):
        """
            Visualizar o plano de estudo por completo 
        """
        pass

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

        return render(request, 'publicacoes/listar.html', dados)
    
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

            return render(request, 'publicacoes/criar.html', dados)
    
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

            return render(request, 'publicacoes/modificar.html', dados)

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
    def listarPorMateria():
        """
        Listar publicações com base em uma materia específica.
        """
        pass
