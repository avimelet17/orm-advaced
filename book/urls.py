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
]