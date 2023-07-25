# Django
from django import forms

# Models
from apps.comentarios.models import Comentario


class CrearFormComentario(forms.ModelForm):
    """Post model form."""
    comentForm = forms.CharField(widget=forms.Textarea)
    class Meta:
        """Form settings."""

        model = Comentario
        fields = ('user', 'post', 'comentario')
