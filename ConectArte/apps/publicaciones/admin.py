from django.contrib import admin
from .models import Publicacion, Imagen, Video
# Register your models here.
admin.site.register(Publicacion)
admin.site.register(Imagen)
admin.site.register(Video)