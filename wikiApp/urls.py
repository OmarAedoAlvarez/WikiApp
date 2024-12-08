from django.urls import path
from . import views

app_name = 'wikiApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('crearTema/', views.crearTema, name='crearTema'),
    path('crearArticulo/', views.crearArticulo, name='crearArticulo'),
    path('verTema/<int:tema_id>/', views.verTema, name='verTema'),
    path('verArticulo/<int:articulo_id>/', views.verArticulo, name='verArticulo'),
    path('buscar/', views.buscarArticulos, name='buscarArticulos')
]
