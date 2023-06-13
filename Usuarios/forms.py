from django import forms
from Usuarios.models import Usuario, Post, Comentario

class UsuarioFormulario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'contraseña', 'email']

class PostFormulario(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'etiqueta', 'contribuyente', 'texto', 'idioma']


class ComentarioFormulario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'post', 'texto']