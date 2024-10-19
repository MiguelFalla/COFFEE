from django.db import models

class Foro(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='noticias/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"

    def __str__(self):
        return f"Titulo: {self.title}"