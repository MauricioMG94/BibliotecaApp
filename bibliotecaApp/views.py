from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Libro, Pais
from .forms import AutorForm, LibroForm, PaisForm
from rest_framework import viewsets
from .serializers import AutorSerializer, LibroSerializer, PaisSerializer
from rest_framework import permissions

#Serializadores
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.BasePermission]


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

# Métodos para Autores
def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'autores/listar.html', {'autores': autores})

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'autores/crear.html', {'form': form})

def editar_autor(request, id):
    autor = get_object_or_404(Autor, id = id)
    if request.method == "POST":
        form = AutorForm(request.POST, instance = autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm(instance = autor)
    return render(request, 'autores/editar.html', {'form': form})

def eliminar_autor(request, id):
    autor = get_object_or_404(Autor, id = id)
    if request.method == "POST":
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'autores/eliminar.html', {'autor': autor})

# Métodos para Libros
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/listar.html', {'libros': libros})

def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/crear.html', {'form': form})

def editar_libro(request, id):
    libro = get_object_or_404(Libro, id = id)
    if request.method == "POST":
        form = LibroForm(request.POST, instance = libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance = libro)
    return render(request, 'libros/editar.html', {'form': form})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id = id)
    if request.method == "POST":
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'libros/eliminar.html', {'libro': libro})

# Métodos para Paises
def lista_paises(request):
    paises = Pais.objects.all()
    return render(request, 'paises/listar.html', {'paises': paises})

def crear_pais(request):
    if request.method == "POST":
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_paises')
    else:
        form = PaisForm()
    return render(request, 'paises/crear.html', {'form': form})

def editar_pais(request, id):
    pais = get_object_or_404(Pais, id = id)
    if request.method == "POST":
        form = PaisForm(request.POST, instance = pais)
        if form.is_valid():
            form.save()
            return redirect('lista_paises')
    else:
        form = PaisForm(instance = pais)
    return render(request, 'paises/editar.html', {'form': form})

def eliminar_pais(request, id):
    pais = get_object_or_404(Pais, id = id)
    if request.method == "POST":
        pais.delete()
        return redirect('lista_paises')
    return render(request, 'paises/eliminar.html', {'pais': pais})