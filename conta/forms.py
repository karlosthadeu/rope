from django import forms
from .models import Usuario
from rope.settings import DATE_INPUT_FORMATS

class CadastroUsuarioForm(forms.ModelForm):

    nome = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Nome completo'}))
    email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'placeholder' 'Email'}))
    data_de_nascimento = forms.DateField(input_formats=DATE_INPUT_FORMATS)
    senha = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar senha'}))
    confirmacaoDeSenha = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar senha'}))

    class Meta:
        model = Usuario

    def clean_password2(self):
        """
            Este método verifica se as senhas correspondem e, caso não 
        """

        senha = self.cleaned_data.get("senha")
        confirmacaoDeSenha = self.cleaned_data.get("confirmacaoDeSenha")

        if senha and confirmacaoDeSenha and senha != confirmacaoDeSenha:
            raise forms.ValidationError("As senhas não correspondem.")

        return confirmacaoDeSenha

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        

        if commit:
            user.save()
        return user