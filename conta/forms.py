from django import forms
from .models import Usuario
from rope.settings import DATE_INPUT_FORMATS

class CadastroUsuarioForm(forms.ModelForm):
    nome = forms.CharField(
        label='', 
        max_length=255, 
        widget=forms.TextInput(attrs={'placeholder': 'Nome completo', 'class': 'form-control'})
    )
    email = forms.EmailField(
        label='', 
        max_length=255, 
        widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
    )
    data_de_nascimento = forms.DateField(
        label='',
        input_formats=DATE_INPUT_FORMATS,
        widget=forms.DateInput(attrs={'placeholder': 'Data de nascimento', 'class': 'form-control'}),
    )
    senha = forms.CharField(
        label='', 
        max_length=255, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar senha', 'class': 'form-control'})
    )
    confirmacao_de_senha = forms.CharField(
        label='', 
        max_length=255, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar senha', 'class': 'form-control'})
    )

    # avatar = forms.ImageField(widget=forms.FileInput(attrs={'id': 'upload', 'class': 'file-input'}))

    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'data_de_nascimento', 'senha', 'confirmacao_de_senha')

    def clean_password2(self):
        """
            Este método verifica se as senhas correspondem e, caso não 
        """

        senha = self.cleaned_data.get("senha")
        confirmacao_de_senha = self.cleaned_data.get("confirmacao_de_senha")

        if senha and confirmacao_de_senha and senha != confirmacao_de_senha:
            raise forms.ValidationError("As senhas não correspondem.")

        return confirmacao_de_senha

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["senha"])

        if commit:
            user.save()
        return user

    



