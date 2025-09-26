from django.shortcuts import render
from django.views.generic import TemplateView
from book import tests as t
from django.test import TestCase
from termcolor import cprint
import random

from book import models as mb
from editorial import models as me

# Colores visibles que soporta termcolor
COLORES = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

# Create your views here.
class ConsultaSinSelectRelated(TemplateView):
    # Vista de nuevo home

    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.querys()
        context['que_estoy_viendo'] = "Consulta Sin select_related"
        return context
    
    @staticmethod
    def querys():
        color = random.choice(COLORES)
        cprint(f'Bad Query', color)
        libro_y_editorial = mb.Libro.objects.filter(editorial__id=1)
        for libro in libro_y_editorial:
            cprint(f'El libro es {libro.titulo}', color)
            cprint(f'La editorial es {libro.editorial.nombre}', color)
            cprint('---------', color)
        cprint("\n\n\n", color)


class ConsultaConSelectRelated(TemplateView):
    # Vista de nuevo home

    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.querys()
        context['que_estoy_viendo'] = "Consulta Con select_related"
        return context
    
    @staticmethod
    def querys():
        color = random.choice(COLORES)
        cprint(f'God Query', color)
        libro_y_editorial = mb.Libro.objects.filter(
            editorial__id=1
        ).select_related('editorial') #? <- Se le agrega
        for libro in libro_y_editorial:
            cprint(f'El libro es {libro.titulo}', color)
            cprint(f'La editorial es {libro.editorial.nombre}', color)
            cprint('---------', color)
            


class ConsultaSinPrefetchRelated(TemplateView):
    # Vista de nuevo home

    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.querys()
        context['que_estoy_viendo'] = "Consulta Sin prefetch_related"
        
        return context
    
    @staticmethod
    def querys():
        color = random.choice(COLORES)
        cprint(f'Bad Query', color)
        libro_y_calificacion = mb.Libro.objects.filter(editorial__id = 1)
        for libro in libro_y_calificacion:
            for cal in libro.libro_calificacion.all():
                print(f'{cal.estrellas} estrellas Calif {cal.calificacion} Editorial {libro.editorial.nombre}')
                
                
class ConsultaConPrefetchRelated(TemplateView):
    # Vista de nuevo home

    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.querys()
        context['que_estoy_viendo'] = "Consulta Con prefetch_related"
        return context
    
    @staticmethod
    def querys():
        color = random.choice(COLORES)
        cprint(f'Bad Query', color)
        libro_y_calificacion = mb.Libro.objects.filter(
            editorial__id = 1
        ).prefetch_related(
            'libro_calificacion'
        )
        for libro in libro_y_calificacion:
            for cal in libro.libro_calificacion.all():
                print(f'{cal.estrellas} estrellas Calif {cal.calificacion}')



class ConsultaConPrefetchYSelectRelated(TemplateView):
    # Vista de nuevo home

    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.querys()
        context['que_estoy_viendo'] = "Consulta Con prefetch_related y select_related"
        return context
    
    @staticmethod
    def querys():
        color = random.choice(COLORES)
        cprint(f'Bad Query', color)
        libro_y_calificacion = mb.Libro.objects.filter(
            editorial__id = 1
        ).prefetch_related(
            'libro_calificacion'
        ).select_related(
            'editorial'
        )
        for libro in libro_y_calificacion:
            for cal in libro.libro_calificacion.all():
                print(f'{cal.estrellas} estrellas Calif {cal.calificacion} Editorial {libro.editorial.nombre}')
                
                
class SinPrefetchBien(TemplateView):
    # Vista de nuevo home

    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.editoriales_con_sus_libros_publicados_sin_Prefetch()
        context['que_estoy_viendo'] = "Consulta Con prefetch_related y select_related"
        return context
    
    @staticmethod
    # Ejemplos usando Prefetch
    def editoriales_con_sus_libros_publicados_sin_Prefetch():

        editoriales = me.Editorial.objects.filter(pk__in=(1, 10, 4)).prefetch_related(
            'libro_editorial'
        )

        for editorial in editoriales:
            print(f'******** Editorial {editorial.nombre} ************')
            print('Libros publicados:')
            for libro in editorial.libro_editorial.all():
                print(
                    f'{libro.isbn} Titulo: {libro.titulo}\n'
                    f'Publicado el: {libro.fecha_publicacion}'
                )
        print('\n')

class SinPrefetchMal(TemplateView):
    # Vista de nuevo home

    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.editoriales_con_sus_libros_publicados_sin_Prefetch()
        context['que_estoy_viendo'] = "Consulta Con prefetch_related y select_related"
        return context
    
    @staticmethod
    # Ejemplos usando Prefetch
    def editoriales_con_sus_libros_publicados_sin_Prefetch():

        editoriales = me.Editorial.objects.filter(pk__in=(1, 10, 4)).prefetch_related(
            'libro_editorial'
        )

        for editorial in editoriales:
            print(f'******** Editorial {editorial.nombre} ************')
            print('Libros publicados:')
            for libro in editorial.libro_editorial.filter(fecha_publicacion__year__gte = 2025):
                print(
                    f'{libro.isbn} Titulo: {libro.titulo}\n'
                    f'Publicado el: {libro.fecha_publicacion}'
                )
        print('\n')



class ConPrefetch(TemplateView):
    # Vista de nuevo home

    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.editoriales_con_sus_libros_publicados_con_Prefetch()
        context['que_estoy_viendo'] = "Consulta Con prefetch_related y select_related"
        return context
    
    @staticmethod
    # Ejemplos usando Prefetch
    def editoriales_con_sus_libros_publicados_con_Prefetch():
        from django.db.models import Prefetch
        
        query_libro = mb.Libro.objects.filter(fecha_publicacion__year__gte=2015)
        libros_prefetch = Prefetch('libro_editorial', queryset=query_libro, to_attr='libros_validos')

        editoriales = me.Editorial.objects.filter(
            pk__in=(1, 2, 3)).prefetch_related(libros_prefetch)

        for editorial in editoriales:
            print(f'******** Editorial {editorial.nombre} ************')
            print('Libros publicados:')
            for libro in editorial.libros_validos:
                print(
                    f'{libro.isbn} Titulo: {libro.titulo}\n'
                    f'Publicado el: {libro.fecha_publicacion}'
                )
            print('\n')
