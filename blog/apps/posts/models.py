from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#Categoria
class Categoria (models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre

#Posteo
class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False, verbose_name="Titulo")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha pub") 
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(null=False, verbose_name="Contenido")
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, default='Sin categoria')
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/post_default.png')
    publicado = models.DateTimeField(default=timezone.now)




class Meta: #orden de las consultas a la BD
    ordering = ('-publicado',)  
    
    def __str__(self):
        return self.titulo

    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()