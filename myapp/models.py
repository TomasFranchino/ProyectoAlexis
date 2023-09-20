from django.db import models
from django.conf import settings
from django.utils import timezone


class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    fav = models.IntegerField(default=0)
    respuesta_a = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='respuestas')

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.texto

    def agregar_fav(self):
        self.fav += 1
        self.save()

    def quitar_fav(self):
        if self.fav > 0:
            self.fav -= 1
            self.save()



'''from django.db import models
from django.conf import settings
from django.utils import timezone

class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    fav = models.IntegerField(default=0)
    
    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.texto
    
    def agregar_fav(self):
        self.fav += 1
        self.save()

    def quitar_fav(self):
        if self.fav > 0:
            self.fav -= 1
            self.save()
            
class Comentario(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    fav = models.IntegerField(default=0)
    
    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.texto
    
    def agregar_fav(self):
        self.fav += 1
        self.save()

    def quitar_fav(self):
        if self.fav > 0:
            self.fav -= 1
            self.save()'''
