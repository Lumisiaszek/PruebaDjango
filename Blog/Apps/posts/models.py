from django.db import models
from django.contrib.auth.models import AbstractUser, User



# usuarios con atributos nuevos
class CustomUser(AbstractUser):
    icono = models.ImageField(upload_to="media/usuarios", null=True, blank=True)
    descripcion = models.TextField(max_length=350)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  
        blank=True,
        help_text='Specific permissions for this user.'
    )    

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Categorias(models.Model):  
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "Categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Posts(models.Model):  
    titulo = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Titulo"
    )
    contenido = models.TextField(verbose_name="Contenido")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="media/posts", null=True, blank=True)

    class Meta:
        db_table = "Posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo


# Con esta forma sólo puedo cargar una imagen
# class Imagenes(models.Model):
#     imagen = models.ImageField(upload_to="/media/Posts")
#     post = models.ForeignKey(Posts, on_delete=models.CASCADE)


class Comentarios(models.Model):
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(max_length=250, verbose_name="Contenido")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)


    # class Meta:
    #     db_table = "Comentarios"  
    #     verbose_name = "Comentario"  
    #     verbose_name_plural = "Comentarios"  
    #     ordering = ['fecha_publicacion'] 

    # def __str__(self):
    #     return f'Comentario de {self.autor} en {self.post.titulo}'
