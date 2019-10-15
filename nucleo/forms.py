from django import forms

# Models:
from .models import Publicacao
from .models import Materia

class PublicacoesForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ('titulo', 'conteudo', 'tags', 'materia')

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ('nome', 'area_de_conhecimento', 'usuario_responsavel')