from django.db import models
from django.forms import ModelForm, TextInput,Textarea,Select
from apps.Usuarios.models import Usuario
from django import forms


# class usuariosForm(ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['NombreUsuario', 'IdTipoUsuario']