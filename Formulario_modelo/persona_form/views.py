from django.shortcuts import render
from django.http import HttpResponse

from .forms import PersonaForm, DocForm

# Create your views here.
def create_doc(request):
  documento = request.POST.get('tipo_doc')
  if request.method == "POST":
    form = 


def index(request):
  if request.method == 'POST':
    form = PersonaForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request, 'index.html', {
        'form': form,
      })
      # return HttpResponse ("Se registro el usuario")
  else :
    form = PersonaForm()
    return render(request, 'index.html', {
      'form' : form,
    })  