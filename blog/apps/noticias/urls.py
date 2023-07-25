
from django.urls import path
from apps.noticias import views

urlpatterns = [

    path(route='',view=views.Listar_Noticias.as_view(), name = 'blog'),
        #view=views.PostsFeedView.as_view(),
        
    path(route='Detalle/<int:pk>',view=views.Detalle_Noticia.as_view(), name = 'detail'),
        #view=views.PostDetailView.as_view(),

    path(route='posts/save_coment', view=views.Comentar_Noticia, name='save_coment' ),
]
