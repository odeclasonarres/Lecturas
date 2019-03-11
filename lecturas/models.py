from django.db import models
from django.utils import timezone

class Lectura(models.Model):
    titulo=models.CharField(max_length=200)
    autor=models.CharField(max_length=200)
    valoracion=models.IntegerField
    categoria=models.CharField(max_length=200)
    tema=models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    lectura_date = created_date = models.DateTimeField(blank=True, null=True))
# Create your models here.
