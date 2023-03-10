from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import *
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormMensajes
from django.views.generic.edit import FormMixin
from django.views.generic import View
from django.contrib.auth import get_user_model
User = get_user_model()

class Inbox(View):
	def get(self, request):
		inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])
		context = {
			"inbox":inbox
		}
		return render(request, 'pages/inbox.html', context)


class CanalFormMixin(FormMixin):
	form_class =FormMensajes

	def get_success_url(self):
		return self.request.path

	def post(self, request, *args, **kwargs):

		if not request.user.is_authenticated:
			raise PermissionDenied

		form = self.get_form()
		if form.is_valid():
			canal = self.get_object()
			usuario = self.request.user 
			mensaje = form.cleaned_data.get("mensaje")
			canal_obj = CanalMensaje.objects.create(canal=canal, usuario=usuario, texto=mensaje)
			
			if request.headers.get('x-requested-with') == 'XMLHttpRequest':
				return JsonResponse({
					'mensaje':canal_obj.texto,
					'username':canal_obj.usuario.username
					}, status=201)

			return super().form_valid(form)

		else:

			if request.headers.get('x-requested-with') == 'XMLHttpRequest':
				return JsonResponse({"Error":form.errors}, status=400)

			return super().form_invalid(form)

class CanalDetailView(LoginRequiredMixin, CanalFormMixin, DetailView):
	template_name= 'pages/canal_detail.html'
	queryset = Canal.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)

		obj = context['object']
		print(obj)


		context['si_canal_mienbro'] = self.request.user in obj.usuarios.all()

		return context



class DetailMs(LoginRequiredMixin, CanalFormMixin, DetailView):

	template_name= 'pages/canal_detail.html'

	def get_object(self, *args, **kwargs):

		username = self.kwargs.get("username")
		mi_username = self.request.user.username
		canal, _ = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)

		if username == mi_username:
			mi_canal, _ = Canal.objects.obtener_o_crear_canal_usuario_actual(self.request.user)

			return mi_canal

		if canal == None:
			raise Http404

		return canal

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