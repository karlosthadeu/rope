from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
# Models
from .models import Publicacao as PublicacaoModel

#Forms
from .forms import PublicacoesForm

# Create your views here.
class PrincipalView():
    @staticmethod
    def index(request):
        dados = {
            'titulo': 'Página inicial',
        }

        return render(request, 'publicacoes/listar.html', dados)

class ChamadosView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')

class HistoricosView():
    pass

class MateriaisView():
    pass

class PlanosDeEstudosView():
    pass

class PublicacoesView():
    # Na primeira verificação tá ok
    @staticmethod
    def listar(request):
        publicacoes = PublicacaoModel.objects.all()
        
        dados = {
            'titulo': 'Listar Publicações',
            'publicacoes': publicacoes 
        }

        return render(request, 'publicacoes/listar.html', dados)
    
    # Na primeira verificação tá ok
    @staticmethod
    def criar(request):
        form = PublicacoesForm(request.POST or None)

        if form.is_valid() :
            form.save()

            return redirect('publicacoes_listar')

        else:
            dados = {
                'titulo': 'Criar Publicação',
                'form': form,
            }

            return render(request, 'publicacoes/criar.html', dados)
    
    # Na primeira verificação tá ok
    @staticmethod
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
            }

            return render(request, 'publicacoes/modificar.html', dados)

    @staticmethod
    def visualizar(request, id):
        return HttpResponse('Visualizar publicação')
    
    @staticmethod
    def apagar(request, id):
        publicacao = get_object_or_404(PublicacaoModel, pk=id)
        publicacao.delete()

        return redirect('publicacoes_listar')