from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

from apps.usuarios.forms import RegistroForm
# Create your views here.

class RegistroForm(FormView):
	#FORMULARIO DJANGO
	form_class = RegistroForm
	success_url = reverse_lazy('users:registrok')
	template_name = 'usuarios/registro.html'
	
	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'usuarios/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'usuarios/logged_out.html'