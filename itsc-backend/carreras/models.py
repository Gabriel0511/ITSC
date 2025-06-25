from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    img = models.ImageField(upload_to='carreras/', null=True, blank=True)

    def __str__(self):
        return self.nombre