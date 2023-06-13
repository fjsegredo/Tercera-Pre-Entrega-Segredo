from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=16, unique=True)
    contraseña = models.CharField(max_length=16)
    email = models.EmailField(max_length=254)
    fecha_de_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    idiomas = (
        ('español', 'Español'),
        ('latín', 'Latín'),
        ('inglés', 'Inglés'),
        ('francés', 'Francés'),
        ('alemán', 'Alemán'),
        ('portugués', 'Portugués'),
        ('griego antiguo', 'Griego antiguo'),
        )
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    etiqueta = models.CharField(max_length=15, blank=True)
    contribuyente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    texto = models.TextField(max_length=9999)
    idioma = models.CharField(max_length=20, choices=idiomas)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)