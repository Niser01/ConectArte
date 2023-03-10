from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from apps.Usuarios.models import *

User = get_user_model()

def user_directory_path(instance, fileName):
    return 'Usuarios/publicaciones/{0}'.format(fileName)
# Create your models here.
class CategoriasVacantes(models.Model):
    IdCategoriaVacante = models.AutoField(primary_key=True)
    CategoriaVacante = models.CharField(max_length=100, null=False, verbose_name="Categoría de la vacante")
    def __str__(self):
        return self.CategoriaVacante



class Vacante(models.Model):
    IdVacante = models.AutoField(primary_key=True)
    CategoriaVacante = models.ForeignKey(CategoriasVacantes, on_delete=models.CASCADE, related_name="autor_vacante")
    AutorVacante = models.ForeignKey(User, on_delete=models.CASCADE, related_name="autor_vacante")
    TituloVacante = models.CharField(max_length=30, blank=False, null=False,  verbose_name="Titulo_Vacante")
    Pago = models.FloatField(null=True, blank=True, verbose_name="Pago")
    DescripcionVacante = models.TextField(blank=False, null=False,  verbose_name="Descripción de la vacante")
    FechaPublicacionVacante = models.DateField(default=timezone.now)
