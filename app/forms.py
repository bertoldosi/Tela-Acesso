from .models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UsuarioForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma senha', widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ('nome', 'email')

    #verificar se as duas senha são iguais
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas informadas não são iguais!')
        return password2

    #inserindo a senha no banco criptografada
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.EmailField()
    class Meta:
        model = Usuario
        fields = ['username', 'password']
