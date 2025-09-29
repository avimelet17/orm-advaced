# Django
from django.urls import path
from django.views.generic.base import View
from book import views

# Viewsalmacenes:renovada
urlpatterns = [
    path(
        route="ConsultaSinSelectRelated",
        view=views.ConsultaSinSelectRelated.as_view(),
        name="home"
    ),
    path(
        route="ConsultaConSelectRelated",
        view=views.ConsultaConSelectRelated.as_view(),
        name="home"
    ),
    path(
        route="ConsultaSinPrefetchRelated",
        view=views.ConsultaSinPrefetchRelated.as_view(),
        name="home"
    ),
    path(
        route="ConsultaConPrefetchRelated",
        view=views.ConsultaConPrefetchRelated.as_view(),
        name="home"
    ),
    path(
        route="ConsultaConPrefetchYSelectRelated",
        view=views.ConsultaConPrefetchYSelectRelated.as_view(),
        name="home"
    ),
    path(
        route="SinPrefetchBien",
        view=views.SinPrefetchBien.as_view(),
        name="home"
    ),
    path(
        route="SinPrefetchMal",
        view=views.SinPrefetchMal.as_view(),
        name="home"
    ),
    path(
        route="ConPrefetch",
        view=views.ConPrefetch.as_view(),
        name="home"
    ),
    path(
        route="TodoEnUno",
        view=views.TodoEnUno.as_view(),
        name="home"
    ),
]