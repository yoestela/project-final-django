
"""Users URLs."""

# Django
from django.urls import path
from django.views.generic import TemplateView
# View
from apps.usuarios import views

urlpatterns = [
    path(
        route='login',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='registro',
        view=views.RegistroForm.as_view(),
        name='registro'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='registro_completado/',
        view=TemplateView.as_view(template_name='usuarios/registrok.html'),
        name='registrok'
    ),
]