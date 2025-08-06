from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=500)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(blank=True, null=True)

    def deg_fecha_hora(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo