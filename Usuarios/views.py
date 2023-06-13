### APP USUARIOS
from django.shortcuts import render
from Usuarios.forms import UsuarioFormulario, PostFormulario, ComentarioFormulario

def vista_crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            contraseña = form.cleaned_data['contraseña']
            email = form.cleaned_data['email']
            form.save()
            return render(request, 'usuario_creado.html', {'nombre': nombre, 'contraseña': contraseña, 'email': email})
    else:
        form = UsuarioFormulario()
    return render(request, 'crear_usuario.html', {'form': form})

def vista_crear_post(request):
    if request.method == 'POST':
        form = PostFormulario(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            etiqueta = form.cleaned_data['etiqueta']
            contribuyente = form.cleaned_data['contribuyente']
            texto = form.cleaned_data['texto']
            form.save()
            return render(request, 'post_creado.html', {'titulo': titulo, 'etiqueta': etiqueta, 'contribuyente': contribuyente, 'texto': texto})
    else:
        form = PostFormulario()
    return render(request, 'crear_post.html', {'form': form})


def vista_comentar(request):
    if request.method == 'POST':
        form = ComentarioFormulario(request.POST)
        if form.is_valid():
            autor = form.cleaned_data['autor']
            post = form.cleaned_data['post']
            texto = form.cleaned_data['texto']
            form.save()
            return render(request, 'comentario_publicado.html', {'autor': autor, 'post': post, 'texto': texto})
    else:
        form = ComentarioFormulario()
    return render(request, 'comentar.html', {'form': form})