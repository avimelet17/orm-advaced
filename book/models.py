from django.db import models as m
from django.utils import timezone

# Create your models here.

class Libro(m.Model):
    isbn = m.CharField(max_length=13, primary_key=True)
    titulo = m.CharField(max_length=70, blank=True)
    editorial = m.ForeignKey(
        "editorial.Editorial",
        related_name='libro_editorial',
        on_delete=m.PROTECT,
    )
    fecha_publicacion = m.DateField(null=True, default=timezone.now())
    imagen = m.URLField(max_length=85, null=True)
    desc_corta = m.CharField(max_length=2000, default='Sin descripción.')
    estatus = m.CharField(max_length=1, default="1")
    categoria = m.CharField(max_length=50, default='Sexo Anal Gore Furro')
     
    
class LibroCalificacion(m.Model):
    libro = m.ForeignKey('book.Libro', related_name='libro_calificacion', on_delete=m.PROTECT)
    estrellas = m.PositiveIntegerField()
    calificacion = m.CharField(max_length=70, blank=True)
