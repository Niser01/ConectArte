from email import message
from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView
from django.contrib.auth import get_user_model
from requests import request
from apps.Usuarios.models import *
from apps.publicaciones.models import *
from django.db.models import Q
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from apps.DM.models import *
from django.core.exceptions import ObjectDoesNotExist


User = get_user_model()


def mensajes_privados(request, username, *args, **kwargs):

	IdUsuario = request.user
	IdUsuarioSeguido = get_object_or_404(User, username=username)

	if not request.user.is_authenticated:
		return HttpResponse("Prohibido")

	canal, created = Canal.objects.obtener_o_crear_canal_ms(IdUsuario, IdUsuarioSeguido)

	if created:
		print("Se ha creado el canal")

	Usuarios_Canal = canal.canalusuario_set.all().values("usuario__username")
	print(Usuarios_Canal)
	mensaje_canal  = canal.canalmensaje_set.all()
	print(mensaje_canal.values("texto"))

	return HttpResponse(f"Nuestro Id del Canal - {canal.id}")




#Vista para abrir la nueva pagina de followers
def followers(request):
    inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])
    proflogued = perfil.objects.get(usuario=request.user)
    context={
        'profreq':proflogued,
        'inbox':inbox,
    }
    return render (request, 'users/followers.html', context)

#Metodo para añadir un seguidor a la cuenta, 
def follow(request, username):
    inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])
    IdUsuario = request.user.id
    IdUsuarioSeguido = get_object_or_404(User, username=username)
    UsuarioSeguido_id=IdUsuarioSeguido.id
    try:
        r1 = SigueA.objects.filter(IdUsuario_id=IdUsuario, IdUsuarioSeguido_id=UsuarioSeguido_id ).get()
    except ObjectDoesNotExist:
        rel = SigueA(IdUsuario_id=IdUsuario, IdUsuarioSeguido_id=UsuarioSeguido_id )
        rel.save()
        
    user = get_object_or_404(User, username=username)
    perfilUsuario = perfil.objects.get(usuario=user)
    proflogued = perfil.objects.get(usuario=request.user)
    mensajes_privados(request, username)
    context={
        'perfil':perfilUsuario,
        'profreq':proflogued,
        'inbox':inbox,
    }
    return render(request, 'users/perfilUsuario.html', context)

#Metodo para eliminar un seguidor a la cuenta, 
def unfollow(request, username):
    inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])
    IdUsuario = request.user
    IdUsuarioSeguido = get_object_or_404(User, username=username)
    UsuarioSeguido_id=IdUsuarioSeguido
    try:
        rel = SigueA.objects.filter(IdUsuario_id=IdUsuario, IdUsuarioSeguido_id=UsuarioSeguido_id ).get()
        rel.delete()
    except ObjectDoesNotExist:
        pass      
    user = get_object_or_404(User, username=username)
    perfilUsuario = perfil.objects.get(usuario=user)
    proflogued = perfil.objects.get(usuario=request.user)
    context={
        'perfil':perfilUsuario,
        'profreq':proflogued,
        'inbox':inbox,
    }
    return render(request, 'users/perfilUsuario.html', context)


def portfolio(request, username):
    inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])
    user = get_object_or_404(User, username=username)
    perfilUsuario = perfil.objects.get(usuario=user)
    postsUser = Publicacion.objects.filter(usuario=user)
    context={
        'perfil':perfilUsuario,
        'postsUser' : postsUser,
        'inbox':inbox,
    }
    return render(request, 'users/portfolio.html', context)

class PortfolioView(View):
    def get(self, request, username, *args, **kwargs):
        inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])
        user = get_object_or_404(User, username=username)
        perfilUsuario = perfil.objects.get(usuario=user)
        postsUser = Publicacion.objects.filter(Autor=user)
        cant_post = len(postsUser)
        context={
            'user':user,
            'perfil':perfilUsuario,
            'postsUser' : postsUser,
            'cant_post': cant_post,
            'inbox':inbox,
        }
        return render(request, 'users/portfolio.html', context)



class ProfileView(View):
   
    def get(self, request, username, *args, **kwargs):
        inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])
        user = get_object_or_404(User, username=username)
        perfilUsuario = perfil.objects.get(usuario=user)
        proflogued = perfil.objects.get(usuario=request.user)
        context={
            'user':user,
            'perfil':perfilUsuario,
            'profreq':proflogued,
            'inbox':inbox,
        }
        return render(request, 'users/perfilUsuario.html', context)

@login_required
def EditProfile(request):
        inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])
        user = request.user.id
        profile = perfil.objects.get(id=user)
        userInfo = User.objects.get(id=user)
        if request.method == 'POST':
            form=UserForm(request.POST, request.FILES, instance=profile)
            Images = request.FILES.getlist('fotoPerfil')
            if form.is_valid():
                for i in Images:
                    image = ImagenPerfil(imagen=i)
                    image.save()
                    userInfo.fotoPerfil.add(image)
                userInfo.first_name = form.cleaned_data.get('first_name')
                userInfo.last_name = form.cleaned_data.get('last_name')
                profile.Descripcion = form.cleaned_data.get('Descripcion')
                profile.Educacion = form.cleaned_data.get('Educacion')
                profile.Experiencia = form.cleaned_data.get('Experiencia')
                profile.Intereses = form.cleaned_data.get('Intereses')
                profile.url = form.cleaned_data.get('url')
                profile.NumeroTelefono = form.cleaned_data.get('NumeroTelefono')
                profile.save()
                userInfo.save()
                return redirect('users:perfil', username=request.user.username)
        else:
            form=UserForm(instance=profile)

        context={
            'form':form,
            'perfil':profile,
            'inbox':inbox,
        }

        return render(request, 'users/editProfile.html', context)