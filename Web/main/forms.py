from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.models import ModelForm
from . models import Room


class FormCreate(ModelForm):
    class Meta:
        model = Room
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'type': 'Text',
                'placeholder': 'Введите Имя',
                'class': 'formimput',
            }),
        }


class UserLogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'Name', 'placeholder': 'Введите имя пользователя', 'class': 'formimput', }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'type': 'Password', 'placeholder': 'Введите пароль', 'class': 'formimput', }))


class UserRegister(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'type': 'Name', 'placeholder': 'Введите имя пользователя', 'class': 'formimput', }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'type': 'password', 'placeholder': 'Введите пароль', 'class': 'formimput', }))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(
        attrs={'type': 'password', 'placeholder': 'Подтвердите пароль', 'class': 'formimput', }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'type': 'Name', 'placeholder': 'Submit Nickname', 'class': 'formimput', }),
            'email': forms.TextInput(attrs={
                'type': 'Email',
                'placeholder': 'Введите эл почту',
                'class': 'formimput',
            }),
            'password1': forms.PasswordInput(attrs={
                'type': 'password',
                'placeholder': 'Введите пароль',
                'class': 'formimput',
            }),
            'password2': forms.PasswordInput(attrs={
                'type': 'password',
                'placeholder': 'Подтвердите пароль',
                'class': 'password',
            }),
        }
