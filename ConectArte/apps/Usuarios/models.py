from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os 
from django.db.models.signals import post_save
from requests import request


def directorioUsuario(instancia, nombreArchivo):
    nombreFotoPerfil = "Usuarios/{0}/profile.jpg.".format(instancia.usuario.username)
    full_path = os.path.join(settings.MEDIA_ROOT, nombreFotoPerfil)
    if os.path.exists(full_path):
        os.remove(full_path)
    return nombreFotoPerfil 

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        perfil.objects.create(usuario=instance)

def guardarPerfil(sender, instance, **kwargs):
    instance.profile.save()

def user_directory_path2(instance, fileName):
    return 'Usuarios/fotoPerfil/{0}'.format(fileName)

class ImagenPerfil(models.Model):
    imagen = models.ImageField(upload_to= user_directory_path2, blank=True, null = True)



class Categorias(models.Model):  
    IdCategoria = models.AutoField(primary_key=True)
    NombreCategoria = models.CharField(max_length=100,verbose_name="Categoría de la vacante", null=False)
    def __str__(self):
        return self.NombreCategoria

class Usuario(AbstractUser):
    IdUsuario = models.CharField(max_length=50)
    fotoPerfil = models.ManyToManyField(ImagenPerfil, blank=True)

    

class perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="profile")
    dateCreated = models.DateField(auto_now_add=True)
    Intereses = models.TextField(blank=False, null=True,  verbose_name="Intereses", default="")
    Educacion = models.TextField(blank=False, null=True,  verbose_name="Educacion", default="")
    Experiencia = models.TextField(blank=False, null=True,  verbose_name="Experiencia", default="")
    Descripcion = models.TextField(blank=False, null=True,  verbose_name="Descripción", default="")
    url = models.CharField(max_length=100, blank=False, null=False)
    NumeroTelefono = models.BigIntegerField(blank=True, null=True)
    def __str__(self):
        return self.usuario.username

    #Se añaden los metodos following y followers para saber que usuarios siguie o quien sigue a ese usuario

    def following(usuario):
        print(usuario)
        user_ids=SigueA.objects.filter(IdUsuario_id=usuario.id).values_list('IdUsuarioSeguido_id')
        Dicc = Usuario.objects.filter(id__in=user_ids) 
        return list(Dicc.values_list('username', flat=True))
        

    def followers(self):
        user_ids=SigueA.objects.filter(IdUsuarioSeguido=self.id).values_list('IdUsuarioSeguido_id', flat=True).distinct()
        return Usuario.objects.filter(id__in=user_ids)  

post_save.connect(create_user_profile, sender=Usuario)
post_save.connect(guardarPerfil, sender=Usuario)


class ClasificaEn(models.Model):
    IdCategoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, verbose_name="Categoria")
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Categoria")

#Se activa la clase SigueA, para poder crear la migracion en la BD.

class SigueA(models.Model):
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='Id_usuario')
    IdUsuarioSeguido = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='Id_usuario_seguido')
    def __str__(self):
        return f'{self.IdUsuario}to{self.IdUsuarioSeguido}'
    class Meta:
        indexes=[ 
            models.Index(fields=['IdUsuario', 'IdUsuarioSeguido',]),
        ]



