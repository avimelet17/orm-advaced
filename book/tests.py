from django.test import TestCase
from termcolor import cprint
import random

from book import models as mb
from editorial import models as me

# Colores visibles que soporta termcolor
COLORES = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

def querys():
    # Selecciona un color diferente en cada ejecución
    color = random.choice(COLORES)
    
    # cprint(f'Bad Query', color)
    # libro_y_editorial = mb.Libro.objects.filter(editorial__id=1)
    # for libro in libro_y_editorial:
    #     cprint(f'El libro es {libro.titulo}', color)
    #     cprint(f'La editorial es {libro.editorial.nombre}', color)
    #     cprint('---------', color)
        
    # print()
    # print()
    # print()
        
    # cprint(f'God Query', color)
    # libro_y_editorial = mb.Libro.objects.filter(
    #     editorial__id=1
    # ).select_related('editorial')
    # for libro in libro_y_editorial:
    #     cprint(f'El libro es {libro.titulo}', color)
    #     cprint(f'La editorial es {libro.editorial.nombre}', color)
    #     cprint('---------', color)


    libro_y_calificacion = mb.Libro.objects.prefetch_related('libro_calificacion').select_related('editorial')
    for libro in libro_y_calificacion:
        for cal in libro.libro_calificacion.all():
            print(f'{cal.estrellas} estrellas Calif {cal.calificacion} Editorial {libro.editorial.nombre}')
            
            
    cprint("\n\n\n", color)
