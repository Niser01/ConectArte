from django.db import models
from apps.Usuarios.models import *
# Create your models here.
class Chat(models.Model):
    IdChat = models.AutoField(primary_key=True)
    NombreChat = models.CharField(max_length=30, blank=False, null=False )

    def __str__(self):
        return self.NombreChat

class Mensajes(models.Model):
    IdMensaje = models.IntegerField()
    IdChat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name="Chat")
    IdUsuarioEmisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    Mensaje = models.TextField(blank=False, null=False,  verbose_name="Mensaje")

class ChateanEn(models.Model):
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    IdChat = models.ForeignKey(Chat, on_delete=models.CASCADE)