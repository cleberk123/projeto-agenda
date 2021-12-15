# from django.db import models
from CONTATOS.models import Contato
from django import forms


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ()
        # Essa exclude é para que não aparece os atributos no form!
