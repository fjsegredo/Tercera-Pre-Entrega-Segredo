from django import forms
from Usuarios.models import Usuario 
from Usuarios.models import Post
from Usuarios.models import Comentario

class Buscar_Por_Contribuyente(forms.Form):
    contribuyente = forms.ModelChoiceField(queryset=Usuario.objects.all())

class Comentario_Por_Autor(forms.Form):
    autor = forms.ModelChoiceField(queryset=Usuario.objects.all())

class Comentarios_En_Post(forms.Form):
    post = forms.ModelChoiceField(queryset=Post.objects.all())