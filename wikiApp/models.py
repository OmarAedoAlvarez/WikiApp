from django.db import models

# Create your models here.
class tema(models.Model):
  nombre = models.CharField(max_length=128, null = True, blank = True)
  descripcionArea = models.CharField(max_length=512, null = True, blank = True)

class articulo(models.Model):
  titulo = models.CharField(max_length=128, null = True, blank = True)
  descripcion = models.CharField(max_length=1024, null = True, blank = True)
  temaRelacionado = models.ForeignKey(tema, null = True, blank = True, on_delete=models.SET_NULL)

