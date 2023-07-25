""" Users models."""

from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    is_medical = models.BooleanField(default=False)
    is_physiotherapist = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user'

class AdminProfile(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='media',blank=True,null=True, default="media/admin-default.png")
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    def __str__(self):
        """Return username."""
        return self.user.username


class ColaboradorProfile(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='media',blank=True,null=True, default="media/colaborador-default.png")
    date_modified = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        """Return username."""
        return self.user.username


class VisitanteProfile(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media',blank=True,null=True, default="media/visitante-default.png")
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'

    def __str__(self):
        """Return username."""
        return self.user.username
