from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from apps.noticias.models import Noticia
from apps.comentarios.models import Comentario
from apps.categorias.models import Categoria
# Forms
#from apps.comentarios.forms import Crear
from django.urls import reverse_lazy

# Forms
from apps.comentarios.forms import CrearFormComentario


class Listar_Noticias(ListView):
    """List."""
    template_name = 'noticias/index.html'
    model = Noticia
    ordering = ('-titulo',)
    paginate_by = 10
    context_object_name = 'posts'
    #para añadir condiciones opcionals
	#queryset = Post.objects.filter(activo=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Categoria.objects.all().order_by('nombre')
        context['categorias'] = cat
        return context

class Detalle_Noticia(DetailView):
    """Detail """
    template_name = 'noticias/detail.html'
    model = Noticia
    context_object_name = 'post'

    
    # def get_queryset(self):
    #return Noticia.objects.filter(Categoria=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['comentarios'] = Comentario.objects.filter(post=self.get_object()).all()
        context['form_coments'] = CrearFormComentario()
        return context


@login_required
def Comentar_Noticia(request):
    if request.method == 'POST':
        post = {
            'user': request.user.id,
            'comentario': request.POST['coment'],
            'post': request.POST['post']
        }
        form = CrearFormComentario(post)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('posts:detail', kwargs={'pk': post}))
    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)
