from django import forms

class Registro(forms.Form):

  nombre = forms.CharField(
    label= "Nombre",
    max_length=50,
    widget=forms.TextInput(attrs={'class': 'input'})
  )
  apellido= forms.CharField(
    label= "Apellido",
    max_length=50,
    widget=forms.TextInput(attrs={'class': 'input'})
  )
  correo = forms.EmailField(
    label= "Correo",
    max_length=50,
    widget=forms.TextInput(attrs={'class': 'input'})
  )
  documento= forms.IntegerField(
    label= "Documento",
    max_length=50,
    widget=forms.TextInput(attrs={'class': 'input'})
  )
  fecha_nacimiento= forms.DateField(required=False)(
    label= "Fecha de nacimiento",
    max_length=50,
    widget=forms.DateTimeInput()
  )
 