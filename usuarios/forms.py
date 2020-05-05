from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(label='Usuário')
    senha = forms.CharField(label='Senha')