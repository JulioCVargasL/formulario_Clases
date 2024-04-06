from django.http      import HttpResponse 
from django.shortcuts import render
from .forms import Contact

def form(request):
  # GET
  if request.method == 'GET':
    form = Contact({
      'first_name': 'Ejemplo: Julio Cesar',
      'last_name' : 'Ejemplo: Vargas Lopez',
      'asunto'    : 'Ejemplo: Inquietud',
      'mensaje'   : 'Ejemplo: Hola mundo !',
    })
    return render(request, 'formulario.html', {
    'formulario': form
    })
  # POST
  if request.method == 'POST':
    return HttpResponse ("Lo logramos enviar")

