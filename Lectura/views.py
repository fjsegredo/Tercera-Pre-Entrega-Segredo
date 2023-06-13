from django.shortcuts import render
from Usuarios.models import Post, Comentario
from Lectura.forms import Buscar_Por_Contribuyente, Comentario_Por_Autor, Comentarios_En_Post

def vista_buscar_por_contribuyente(request):
    if request.method == 'POST':
        form = Buscar_Por_Contribuyente(request.POST)
        if form.is_valid():
            contribuyente = form.cleaned_data['contribuyente']
            posts = Post.objects.filter(contribuyente=contribuyente)
            return render(request, 'resultadosporcontribuyente.html', {'posts': posts, 'contribuyente': contribuyente})
    else:
        form = Buscar_Por_Contribuyente()
    return render(request, 'buscarporcontribuyente.html', {'form': form})

def vista_comentario_por_autor(request):
    if request.method == 'POST':
        form = Comentario_Por_Autor(request.POST)
        if form.is_valid():
            autor = form.cleaned_data['autor']
            comentarios = Comentario.objects.filter(autor=autor)
            return render(request, 'resultadoscomentarioporautor.html', {'comentarios': comentarios, 'autor': autor})
    else:
        form = Comentario_Por_Autor()
    return render(request, 'buscarcomentarioporautor.html', {'form': form})

def vista_comentarios_en_post(request):
    if request.method == 'POST':
        form = Comentarios_En_Post(request.POST)
        if form.is_valid():
            post = form.cleaned_data['post']
            comentarios = Comentario.objects.filter(post=post)
            return render(request, 'resultadoscomentariosenpost.html', {'comentarios': comentarios, 'post': post})
    else:
        form = Comentarios_En_Post()
    return render(request, 'vercomentariosenpost.html', {'form': form})