from django.db import models as m

# Create your models here.

class Libro(m.Model):
    isbn = m.CharField(max_length=13, primary_key=True)
    titulo = m.CharField(max_length=70, blank=True)
    editorial = m.ForeignKey(
        "editorial.Editorial",
        related_name='libro_editorial',
        on_delete=m.PROTECT,
    )
