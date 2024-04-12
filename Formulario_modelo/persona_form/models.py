from django.db import models

# Create your models here.
class Doc_type(models.Model):
  type      = models.CharField(max_length=50)
  def __str__(self):
    return self.type

class Persona(models.Model):
  nombre    = models.CharField(max_length=50)
  apellido  = models.CharField(max_length=50)
  correo    = models.EmailField()
  tipo_doc  = models.ForeignKey(Doc_type, on_delete=models.PROTECT, null= False)