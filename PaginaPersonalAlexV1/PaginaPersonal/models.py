from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Conexiones(models.Model):
    numeroConexiones = models.IntegerField()
    fecha = models.DateTimeField(null=False)
    ip = models.TextField(max_length=100, blank=False)
    pais = models.TextField(max_length=100, blank=False)
    ciudad = models.TextField(max_length=100, blank=False)
    postcode = models.TextField(max_length=100, blank=False)
    coordenadas = models.TextField(max_length=100, blank=False)
    def __str__(self):
        return '{} in {}'.format(self.ip, self.postcode)
