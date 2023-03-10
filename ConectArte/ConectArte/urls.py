"""ConectArte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from apps.vacantes.views import *
from .views import HomeView, home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name = 'home'),
    path('', home),
    path('accounts/', include('allauth.urls')),
    path('users/', include('apps.Usuarios.urls', namespace ="users")),
    path('search/', include('apps.Buscador.urls', namespace='search')),
    path('publicacion/', include('apps.publicaciones.urls', namespace='publicacion')),
    path('vacantes/', VacanteView.as_view(), name="vacante"),
    path('dm/', include('apps.DM.urls', namespace='dm')),
    
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
