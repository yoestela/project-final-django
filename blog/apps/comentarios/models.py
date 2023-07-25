""" Comments models."""
from django.db import models
from apps.usuarios.models import Usuario
from apps.noticias.models import Noticia

# Model

# Create your models here.
class Comentario(models.Model):
    """Comentario model."""
    
    user = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    post = models.ForeignKey(Noticia, on_delete=models.PROTECT)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    comentario = models.CharField(max_length=5000)

    class Meta:
        ordering = ('fecha_creacion',)

    def __str__(self):
        return self.comentario
