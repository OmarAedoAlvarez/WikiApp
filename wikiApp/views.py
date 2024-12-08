from django.shortcuts import render
from .models import articulo,tema
from django.db.models import Q
# Create your views here.
def index(request):
    temas = tema.objects.all()
    return render(request, 'index.html',{'temas':temas})    

def crearTema(request):
    if request.method == "POST":
        nombre = request.POST.get("nombreTema")
        descripcionArea = request.POST.get("descripcionArea")
        tema.objects.create(nombre=nombre, descripcionArea=descripcionArea)
    return render(request, 'crearTema.html', {
        'temas': tema.objects.all()
    })    

def crearArticulo(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        tema_id = request.POST.get("tema")
        temaRelacionado = tema.objects.get(id = tema_id)
        articulo.objects.create(titulo=titulo, descripcion=descripcion, temaRelacionado=temaRelacionado)
    return render(request, 'crearArticulo.html', {'temas': tema.objects.all()})

def verTema(request, tema_id):
    temaActual = tema.objects.get(id=tema_id)  
    listaArticulos = temaActual.articulo_set.all()  
    return render(request, 'verTema.html', {
        'tema': temaActual,  
        'articulosRelacionados': listaArticulos,
        'temas': tema.objects.all()
    })

def verArticulo(request, articulo_id):
    articuloActual = articulo.objects.get(id=articulo_id)  
    return render(request, 'verArticulo.html', {
        'articulo': articuloActual,
        'temas': tema.objects.all()
    })

def buscarArticulos(request):
    query = request.GET.get('q', '')
    resultados = []
    
    if query:
        resultados = articulo.objects.filter(titulo__icontains=query)
    
    temas = tema.objects.all() 
    return render(request, 'buscar.html', {
        'query': query,
        'resultados': resultados,
        'temas': temas
    })