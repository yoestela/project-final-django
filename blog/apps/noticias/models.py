"""Noticias models."""

from django.db import models
from ckeditor.fields import RichTextField

from apps.usuarios.models import Usuario
from apps.categorias.models import Categoria

class Noticia(models.Model):
	user = models.ForeignKey( Usuario, on_delete = models.PROTECT )
	titulo = models.CharField(max_length=255, null=False)
	subtitulo = models.CharField(max_length=255, null=True, blank=True)
	imagen = models.ImageField(null=True, blank=True, upload_to = 'noticias', default='static/post-default.png')
	texto = RichTextField(null=False)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	activo = models.BooleanField(default=True)
	categoria_noticia = models.ManyToManyField(Categoria, null=True, default='Sin Categoria')
        
	class Meta:
		ordering = ('titulo',)
    
	def __str__(self):
		return '{} por @{}'.format(self.titulo, self.user.username)
	def save(self, *args, **kwargs):
		super().save(*args,**kwargs)