from django.contrib import admin
from apps.comentarios.models import Comentario

@admin.register(Comentario)
class ComentariosAdmin(admin.ModelAdmin):
    """Comentario admin."""

    list_display = ('id', 'fecha_creacion', 'user', 'post', 'comentario')

