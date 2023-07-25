from django.db import models

class Categoria(models.Model):
    """Categoria model."""
    
    nombre = models.CharField(max_length=100,unique=True, null=False)
    descripcion = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre
