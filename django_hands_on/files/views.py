from django.shortcuts import render
from django.views.generic import TemplateView
from benvinguda.models import WelcomeFrase
from random import choice

# Create your views here.
class HomeView(TemplateView):
    """First page view"""
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        """Put the 'welcome' in context, template will show it."""
        context = {
            'welcome': choice(WelcomeFrase.objects.all()).missatge,
        }
        return self.render_to_response(context)

