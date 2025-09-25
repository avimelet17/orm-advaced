# Django
from django.urls import path
from django.views.generic.base import View
from book import views

# Viewsalmacenes:renovada
urlpatterns = [
    path(
        route="",
        view=views.HomeView.as_view(),
        name="home"
    )
]