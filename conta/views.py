from django.shortcuts import render, redirect
from .forms import CadastroUsuarioForm

# Create your views here.
class UsuarioView():
    @staticmethod
    def criar(request):
        form = CadastroUsuarioForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('entrar')
        
        else:
            dados = {
                'titulo': 'Cadastre-se!',
                'form': form,
            }

            return render(request, 'registration/cadastro.html', dados)
    

