"""blog URL Configuration """

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
        
    path('', include(('apps.noticias.urls', 'noticias'), namespace='posts')),

    path(route='about',view=TemplateView.as_view(template_name='about.html'), name='about'),

    path('', include(('apps.usuarios.urls', 'usuarios'), namespace='users')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

