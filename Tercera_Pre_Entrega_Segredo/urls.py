"""
URL configuration for Tercera_Pre_Entrega_Segredo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Usuarios.views import vista_crear_usuario, vista_crear_post, vista_comentar
from Lectura.views import vista_buscar_por_contribuyente, vista_comentario_por_autor, vista_comentarios_en_post
from .views import vista_base, vista_inicio


urlpatterns = [
    path('', vista_inicio, name='inicio'),
    path('base/', vista_base, name='base'),
    path('admin/', admin.site.urls),
    path('crear_usuario/', vista_crear_usuario, name="crear_usuario"),
    path('crear_post/', vista_crear_post, name="crear_post"),
    path('comentar/', vista_comentar, name='comentar'),
    path('buscarporcontribuyente/', vista_buscar_por_contribuyente, name='buscar_por_contribuyente'),
    path('buscarcomentarioporautor/', vista_comentario_por_autor, name='buscar_comentario_por_autor'),
    path('vercomentariosenpost/', vista_comentarios_en_post, name='vercomentariosenpost'),
]

