from __future__ import unicode_literals

from django.db import models

# Create your models here.

class WelcomeFrase(models.Model):
    """Sentences to greet the user.

    The application contains a list of sentences and, randomly, one will
    be used in order to greet the user (at the main page).
    """
    class Meta(object):
        verbose_name = "frase de benvinguda"
        verbose_name_plural = "frases de benvinguda"

    missatge = models.CharField('missatge', max_length=100)
    only_anonymous = models.BooleanField('nomes per anonims', default=True)
