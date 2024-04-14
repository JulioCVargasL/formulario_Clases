from django.shortcuts import render
from django.http import HttpResponse

from .forms import PersonaForm, DocForm

# Create your views here.
def create_doc(request):
  if request.method == "POST":
    form = DocForm(request.POST)
    if form.is_valid():
      form.save()
      form = DocForm()
  else:
    form = DocForm()
  return render(request, 'documento.html',{'form':form})


def index(request):
  if request.method == 'POST':
    form = PersonaForm(request.POST)
    if form.is_valid():
      form.save()
      form = PersonaForm()
      return render(request, 'index.html', {
        'form': form,
      })
    else:
      return render(request, 'index.html', {
      'form' : form,
      })  
      # return HttpResponse ("Se registro el usuario")
  else :
    form = PersonaForm()
    return render(request, 'index.html', {
      'form' : form,
    })  