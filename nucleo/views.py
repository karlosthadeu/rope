from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

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
    def alterar(request, id):
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

            return render(request, 'plano_de_estudo/modificarNome.html', dados)

    @staticmethod
    @login_required(redirect_field_name='entrar')
    def apagar_publicacao_do_Plano():
        """
            Apaga uma publicação do plano de estudo
        """
        pass

    @staticmethod
    @login_required(redirect_field_name='entrar')
    def adicionar_publicacao_ao_plano():
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
    def visualizar():
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
    def listar_por_materia(request, materia_id):
        """
        Listar publicações com base em uma materia específica.
        """
<<<<<<< HEAD
        publicacoes = PublicacaoModel.objects.filter(MateriaForm__id = materia_id).order_by('-id')[0]

        dados = {
            'titulo': 'Listar Publicações por matéria',
            'publicacoes': publicacoes,
        }

        return 
=======
        pass
>>>>>>> 75e1ca31600d46b9fdd2631c458bce682a498e6a
