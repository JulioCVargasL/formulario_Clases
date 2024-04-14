from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_documento', views.create_doc, name='crear_documento')
]
