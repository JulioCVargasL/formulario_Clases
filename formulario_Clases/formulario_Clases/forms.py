from django import forms

SELECTOR_URGENCIA = {
  "1":"Bajo",
  "2":"Medio",
  "3":"Alto",
}

class Contact(forms.Form):

  first_name  = forms.CharField(
    label="Nombre", 
    max_length=50,
    widget=forms.TextInput(attrs={'class': 'input'}),
    )
  
  last_name   = forms.CharField(
    label="Apellidos", 
    max_length=50,
    widget=forms.TextInput(attrs={'class': 'input'})
    )
  
  asunto      = forms.CharField(
    label="Asunto",
    max_length=50,
    widget=forms.TextInput(attrs={'class': 'input'})
    )
  
  mensaje     = forms.CharField( 
    max_length=50,
    label="Mensaje",
    widget=forms.TextInput(attrs={'class': 'input'})
    )
  
  prioridad   = forms.ChoiceField(
    choices=SELECTOR_URGENCIA,
    widget=forms.Select(attrs={'class': 'input'})
  )
  
