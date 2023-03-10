from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView
from django.contrib.auth import get_user_model
from apps.Usuarios.models import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ComentarioForm
from apps.DM.models import *

# Create your views here.
class commentView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])
        post = Publicacion.objects.get(pk=pk)
        form = ComentarioForm()
        comments = Comentarios.objects.filter(IdPublicacion=post).order_by('-FechaComment')
        context = {
            'post': post,
            'form': form,
            'comments':comments,
            'inbox':inbox,
        }
        return render(request, 'pages/comments.html', context)

    def post(self, request, pk, *args, **kwargs):
        inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])
        post = Publicacion.objects.get(pk=pk)
        form = ComentarioForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.IdUsuario = request.user
            new_comment.IdPublicacion = post
            new_comment.save()

        comments = Comentarios.objects.filter(IdPublicacion=post).order_by('-FechaComment')
        context = {
            'post': post,
            'form': form,
            'comments':comments,
            'inbox':inbox,
        }

        return render(request, 'pages/comments.html', context)