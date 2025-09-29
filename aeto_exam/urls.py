# Django
from django.urls import path
from aeto_exam import colin

# Django
from django.urls import path
from aeto_exam.views import enano, siento_que_olvide_a_alguien, zorra

gran_colin = [
    path(
        route="colin/Caso1LibrosConEditorial",
        view=colin.Caso1LibrosConEditorial.as_view(),
    ),
    path(
        route="colin/Caso2CalificacionesConLibro",
        view=colin.Caso2CalificacionesConLibro.as_view(),
    ),
    path(
        route="colin/Caso3AutoresConLibros",
        view=colin.Caso3AutoresConLibros.as_view(),
    ),
    path(
        route="colin/Caso4ValuesEjemplo",
        view=colin.Caso4ValuesEjemplo.as_view(),
    ),
    path(
        route="colin/Caso5OnlyEjemplo",
        view=colin.Caso5OnlyEjemplo.as_view(),
    ),
    path(
        route="colin/Caso6DeferEjemplo",
        view=colin.Caso6DeferEjemplo.as_view(),
    ),
    path(
        route="colin/Caso7AutoresLibrosEditorial",
        view=colin.Caso7AutoresLibrosEditorial.as_view(),
    ),
]


los_demas = [
    # =====================
    # Rutas para enano.py
    # =====================
    path("enano/Caso1LibrosConEditorial", enano.Caso1LibrosConEditorial.as_view()),
    path("enano/Caso2CalificacionesConLibro", enano.Caso2CalificacionesConLibro.as_view()),
    path("enano/Caso3AutoresConLibros", enano.Caso3AutoresConLibros.as_view()),
    path("enano/Caso4ValuesEjemplo", enano.Caso4ValuesEjemplo.as_view()),
    path("enano/Caso5OnlyEjemplo", enano.Caso5OnlyEjemplo.as_view()),
    path("enano/Caso6DeferEjemplo", enano.Caso6DeferEjemplo.as_view()),
    path("enano/Caso7AutoresLibrosEditorial", enano.Caso7AutoresLibrosEditorial.as_view()),

    # ===================================
    # Rutas para siento_que_olvide_a_alguien.py
    # ===================================
    path("alguien/Caso1LibrosConEditorial", siento_que_olvide_a_alguien.Caso1LibrosConEditorial.as_view()),
    path("alguien/Caso2CalificacionesConLibro", siento_que_olvide_a_alguien.Caso2CalificacionesConLibro.as_view()),
    path("alguien/Caso3AutoresConLibros", siento_que_olvide_a_alguien.Caso3AutoresConLibros.as_view()),
    path("alguien/Caso4ValuesEjemplo", siento_que_olvide_a_alguien.Caso4ValuesEjemplo.as_view()),
    path("alguien/Caso5OnlyEjemplo", siento_que_olvide_a_alguien.Caso5OnlyEjemplo.as_view()),
    path("alguien/Caso6DeferEjemplo", siento_que_olvide_a_alguien.Caso6DeferEjemplo.as_view()),
    path("alguien/Caso7AutoresLibrosEditorial", siento_que_olvide_a_alguien.Caso7AutoresLibrosEditorial.as_view()),

    # =====================
    # Rutas para zorra.py
    # =====================
    path("zorra/Caso1LibrosConEditorial", zorra.Caso1LibrosConEditorial.as_view()),
    path("zorra/Caso2CalificacionesConLibro", zorra.Caso2CalificacionesConLibro.as_view()),
    path("zorra/Caso3AutoresConLibros", zorra.Caso3AutoresConLibros.as_view()),
    path("zorra/Caso4ValuesEjemplo", zorra.Caso4ValuesEjemplo.as_view()),
    path("zorra/Caso5OnlyEjemplo", zorra.Caso5OnlyEjemplo.as_view()),
    path("zorra/Caso6DeferEjemplo", zorra.Caso6DeferEjemplo.as_view()),
    path("zorra/Caso7AutoresLibrosEditorial", zorra.Caso7AutoresLibrosEditorial.as_view()),
]

urlpatterns = []

urlpatterns.extend(gran_colin)
urlpatterns.extend(los_demas)
