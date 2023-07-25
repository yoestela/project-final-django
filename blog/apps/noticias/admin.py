from django.contrib import admin

from .models import Categoria, Noticia

@admin.register (Noticia)

class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('id','fecha_creacion', 'user', 'titulo', 'subtitulo','imagen','activo')
    search_fields = ('titulo', 'user__username')
    list_filter = ('fecha_creacion','titulo','user', 'categoria_noticia')
        
        
    def get_form(self, request, obj=None, **kwargs):
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        #form.base_fields['profile'].initial = request.user.profile
        return form
