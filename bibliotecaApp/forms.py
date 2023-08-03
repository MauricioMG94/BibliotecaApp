from django import forms
from .models import Autor, Libro, Pais

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'pais_nacimiento', 'edad']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'anio_edicion', 'paginas', 'idioma', 'editorial']