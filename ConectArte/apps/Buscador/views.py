from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView
from django.contrib.auth import get_user_model
from apps.Usuarios.models import *
from django.db.models import Q
from apps.DM.models import *

class SearchArtist(View):
    def get(self, request, *args, **kwargs):
        inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])
        query = self.request.GET.get('query')
        perfiles = perfil.objects.filter(Q(usuario__username__icontains=query))
        context={
            'perfiles':perfiles,
            'inbox':inbox,
        }
        return render(request, 'pages/search.html', context)

# Create your views here.
