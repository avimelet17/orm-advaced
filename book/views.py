from django.shortcuts import render
from django.views.generic import TemplateView
from book import tests as t

# Create your views here.
class HomeView(TemplateView):
    # Vista de nuevo home

    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        t.querys()
        return context