from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True,null=True)
    
    
    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.texto
    '''
    fav = models.IntegerField(default=0)
    def agregar_fav(self):
        self.fav += 1
        self.save()

    def quitar_fav(self):
        if self.fav > 0:
            self.fav -= 1
            self.save()
            
class Comentario(Publicacion):
     id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)'''
