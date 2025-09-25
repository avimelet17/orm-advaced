from django.db import models as m

# Create your models here.
class Editorial(m.Model):
    nombre = m.CharField(max_length=100)
    pais = m.CharField(max_length=100, null=True)
