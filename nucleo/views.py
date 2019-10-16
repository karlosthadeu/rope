from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Models
from .models import Publicacao as PublicacaoModel
from .models import Materia as MateriaModel

#Forms
from .forms import PublicacoesForm
from .forms import MateriaForm

# Create your views here.
class PrincipalView():
    @staticmethod
    def inicio(request):
        dados = {
            'titulo': 'Página inicial',
        }

        return render(request, 'principal/inicio.html', dados)

class ChamadosView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')

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
            return HttpResponse('Deu certo') # Alterar essa linha para redirecionar para uma página específica.
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
            return HttpResponse('Deu certo') # Alterar essa linha para redirecionar para uma página específica.
        else:
            dados = {
                'titulo': 'Criar Matéria',
                'form': form
            }

            return render(request, 'materias/criar.html', dados)

class PlanosDeEstudosView():
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
    def listar_por_materia(request, materia_id):
        """
        Listar publicações com base em uma materia específica.
        """
        publicacoes = PublicacaoModel.objects.filter(MateriaForm__id = materia_id).order_by('-id')[0]

        dados = {
            'titulo': 'Listar Publicações por matéria',
            'publicacoes': publicacoes,
        }

        return 