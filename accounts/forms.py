from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nama Pengguna', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Pengguna Anda'}))
    password = forms.CharField(label='Kata Sandi', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Kata Sandi Anda'}))