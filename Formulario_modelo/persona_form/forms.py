from django.forms import ModelForm
from .models import Persona, Doc_type

class DocForm(ModelForm):
  class Meta:
    model   = Doc_type
    fields  = ("__all__")

class PersonaForm(ModelForm):

  class Meta:
    model   = Persona
    fields  = ("__all__")