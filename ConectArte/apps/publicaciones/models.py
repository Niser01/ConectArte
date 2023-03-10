from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from apps.Usuarios.models import *
from .validators import file_size



User = get_user_model()

def user_directory_path(instance, fileName):
    return 'Usuarios/publicaciones/{0}'.format(fileName)

# def dm_directory_path(instance, fileName):
#     return 'Usuarios/mensajes/{0}'

# Create your models here.
class CategoriaPublicacion(models.Model):
    IdCatePub = models.AutoField(primary_key=True)
    NombreCatPub = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return self.NombreCatPub
class Imagen(models.Model):
    imagen = models.ImageField(upload_to= user_directory_path, blank=True, null = True)

class Video(models.Model):
    video=models.FileField(upload_to= user_directory_path, blank=True, null = True)

class Publicacion(models.Model):
    IdPublicacion = models.AutoField(primary_key=True)
    Autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="autor_publicacion")
    Titulo = models.CharField(max_length=30, blank=False, null=False,  verbose_name="Titulo")
    DescripcionPublicacion = models.TextField(blank=False, null=False,  verbose_name="Descripción de la publicación")
    Multimedia_Img = models.ManyToManyField(Imagen, blank=True)
    Multimedia_Video = models.ManyToManyField(Video, blank=True, validators=[file_size])
    FechaPublicacion = models.DateField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name="likes")
    dislikes = models.ManyToManyField(User, blank=True, related_name="dislikes")

class Comentarios(models.Model):
    IdComentario = models.AutoField(primary_key=True)
    IdUsuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="autor_comentario")
    IdPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    Comentario = models.TextField(blank=False, null=False)
    FechaComment = models.DateField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name="comment_likes")
    dislikes = models.ManyToManyField(User, blank=True, related_name="comment_dislikes")

class PerteneceACategoria(models.Model):
    IdPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    IdCatePub = models.ForeignKey(CategoriaPublicacion, on_delete=models.CASCADE)



