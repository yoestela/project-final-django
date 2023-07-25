from django.contrib import admin
from apps.categorias.models import Categoria

@admin.register(Categoria)

class CategoriaAdmin(admin.ModelAdmin):
    """Categoria admin."""

    list_display = ('id', 'nombre','descripcion')
