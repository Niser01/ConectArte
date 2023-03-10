from django import forms 
from .models import *

class VacanteForm(forms.ModelForm):
    
    DescripcionVacante = forms.CharField(widget=forms.Textarea(attrs={
            'class':"form-control", 'id':"exampleFormControlTextarea1",
            'rows': '6',
            'placeholder': 'Describe el trabajo a realizar:'
            }),
        required=True)
    TituloVacante = forms.CharField(widget=forms.Textarea(attrs={
            'class':"form-control", 'id':"exampleFormControlTextarea1",
            'rows': '1',
            'placeholder': 'Titulo de la vacante:'
            }),
        required=True)

    class Meta:
        model = Vacante 
        fields = ['CategoriaVacante','DescripcionVacante', 'Pago']