from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.db.models import Prefetch
from autor.models import Autor
from book.models import Libro, LibroCalificacion
from editorial.models import Editorial

# --- Caso 1 ---
class Caso1LibrosConEditorial(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.libros_con_editorial()
        context['que_estoy_viendo'] = "Caso 1: Libros con su editorial"
        return context

    @staticmethod
    def libros_con_editorial():
        libros = Libro.objects.all().select_related('editorial').only('titulo','editorial__nombre')
        for libro in libros:
            print(libro.titulo, libro.editorial.nombre)

        """
        PROBLEMA:
        - Esto genera un N+1 (una query para libros y otra por cada editorial).
        EJERCICIO:
        - Optimízalo
        """


# --- Caso 2 ---
class Caso2CalificacionesConLibro(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.calificaciones_con_libro()
        context['que_estoy_viendo'] = "Caso 2: Calificaciones con su libro"
        return context

    @staticmethod
    def calificaciones_con_libro():
        califs = LibroCalificacion.objects.select_related('libro').only('estrellas', 'libro__titulo')
        for c in califs:
            print(c.estrellas, "->", c.libro.titulo)

        """
        PROBLEMA:
        - Cada acceso a c.libro dispara otra query (N+1).
        EJERCICIO:
        - Optimízalo
        """


# --- Caso 3 ---
class Caso3AutoresConLibros(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.autores_con_libros()
        context['que_estoy_viendo'] = "Caso 3: Autores con sus libros"
        return context

    @staticmethod
    def autores_con_libros():
        autores = Autor.objects.all().prefetch_related('book').only('name', 'book__titulo')
        for a in autores:
            print(a.name, [libro.titulo for libro in a.book.all()])

        """
        PROBLEMA:
        - Autor → Libro es ManyToMany. Cada .book.all() dispara queries extra.
        EJERCICIO:
        - Optimízalo
        """


# --- Caso 4 ---
class Caso4ValuesEjemplo(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.values_ejemplo()
        context['que_estoy_viendo'] = "Caso 4: values() ejemplo"
        return context

    @staticmethod
    def values_ejemplo():
        datos = Libro.objects.only("isbn", "titulo", "editorial__nombre")
        for d in datos:
            print(d)

        """
        PROBLEMA:
        - values() devuelve dicts, no instancias de modelos.
        EJERCICIO:
        - Reescribe
        """


# --- Caso 5 ---
class Caso5OnlyEjemplo(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.only_ejemplo()
        context['que_estoy_viendo'] = "Caso 5: only() ejemplo"
        return context

    @staticmethod
    def only_ejemplo():
        libros = Libro.objects.select_related('editorial').only("titulo", 'editorial__nombre')
        for l in libros:
            print(l.titulo, l.editorial.nombre)

        """
        PROBLEMA:
        - only("titulo") carga solo titulo. Acceder a editorial dispara query extra.
        EJERCICIO:
        - Ajusta
        """


# --- Caso 6 ---
class Caso6DeferEjemplo(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.defer_ejemplo()
        context['que_estoy_viendo'] = "Caso 6: defer() ejemplo"
        return context

    @staticmethod
    def defer_ejemplo():
        libros = Libro.objects.only("titulo")
        for l in libros:
            print(l.titulo)

        """
        PROBLEMA:
        - defer() no es error, pero todavía carga casi todo.
        EJERCICIO:
        - Combina
        """


# --- Caso 7 ---
class Caso7AutoresLibrosEditorial(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.autores_libros_editorial()
        context['que_estoy_viendo'] = "Caso 7: Autores con libros y editorial"
        return context

    @staticmethod
    def autores_libros_editorial():
        query = Libro.objects.select_related('editorial').only('titulo', 'editorial__nombre')
        info_prefetch = Prefetch('book', queryset=query, to_attr='info')
        
        autores = Autor.objects.all().prefetch_related(info_prefetch).only('name')
        
        for a in autores:
            for l in a.info:
                print(a.name, l.titulo, l.editorial.nombre)

        """
        PROBLEMA:
        - N+1 por autores, N+1 por libros y otro N+1 por editoriales.
        EJERCICIO:
        - Optimízalo
        """
