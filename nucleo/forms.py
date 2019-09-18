from django import forms
from .models import Publicacao

class PublicacoesForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ('titulo', 'conteudo', 'tags', 'materia')