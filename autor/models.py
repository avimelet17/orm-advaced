from django.db import models as m

# Create your models here.
class Autor(m.Model):
    name = m.CharField(default='Nombre')
    book = m.ManyToManyField('book.Libro',related_name='libros_autores')