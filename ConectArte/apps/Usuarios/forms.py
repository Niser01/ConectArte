from django.db import models
from django.forms import ModelForm, TextInput,Textarea,Select
from apps.Usuarios.models import Usuario
from django import forms

from .models import perfil

class UserForm(forms.ModelForm):
    fotoPerfil = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class':"block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300 ",
        'multiple': False,
        'title':"uploadfile"
        }),
        required=False  
        )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            }),
            required=False
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            }),
            required=False
    )
    Descripcion = forms.CharField(widget=forms.Textarea(attrs={
            'class':"form-control", 'id':"exampleFormControlTextarea1",
            'rows': '6',
            'placeholder': 'Escribe tu publicación:'
            }),
        required=False)
    
    Educacion = forms.CharField(widget=forms.Textarea(attrs={
        'class':"form-control", 'id':"exampleFormControlTextarea1",
        'rows': '6',
        'placeholder': 'Escribe tu publicación:'
        }),
    required=False)

    Experiencia = forms.CharField(widget=forms.Textarea(attrs={
        'class':"form-control", 'id':"exampleFormControlTextarea1",
        'rows': '6',
        'placeholder': 'Escribe tu publicación:'
        }),
    required=False)
    
    Intereses = forms.CharField(widget=forms.Textarea(attrs={
            'class':"form-control", 'id':"exampleFormControlTextarea1",
            'rows': '6',
            'placeholder': 'Escribe tu publicación:'
            }),
        required=False)
    
    url = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            }),
            required=False
    )
        
    
    NumeroTelefono = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            }),
             required=False
    )

    class Meta:
        model = perfil
        fields = ('Descripcion', 'Educacion','Experiencia','Intereses','url','NumeroTelefono')

