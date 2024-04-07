from django.db import models
from datetime import date

# Create your models here.

class Documento(models.Model):

  tipo = models.CharField(max_length=50)

class Persona(models.Model):

  nombre            = models.CharField(max_length=50)
  apellido          = models.CharField(max_length=50)
  correo            = models.EmailField()
  documento         = models.IntegerField()
  fecha_nacimiento  = models.DateTimeField(auto_now=False, auto_now_add=False)

  documento         = models.ForeignKey(Documento, on_delete=models.PROTECT)
