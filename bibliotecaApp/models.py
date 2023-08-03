from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Pais(models.Model):
    nombre = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=75)
    pais_nacimiento = models.ForeignKey(Pais, on_delete=models.CASCADE)
    edad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    anio_edicion = models.IntegerField()
    paginas = models.IntegerField(validators=[MinValueValidator(1)])
    idioma = models.CharField(max_length=20)
    editorial = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
