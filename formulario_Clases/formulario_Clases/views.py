from django.http      import HttpResponse 
from django.shortcuts import render

def form(request):
  return render(request, 'formulario.html', {})

