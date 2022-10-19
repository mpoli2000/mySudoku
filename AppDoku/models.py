from socket import NI_NUMERICHOST
from django.db import models

# Create your models here.

class MiJuego(models.Model):
    fecha = models.DateField()
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length = 200)
    nivel = models.IntegerField(default=1)
    sudoku_inicial = models.CharField(max_length=81)
    sudoku_final = models.CharField(max_length=81)
    numeros = models.IntegerField()
    ceros = models.IntegerField()
    progreso = models.FloatField(default=0)
    movimientos = models.IntegerField(default=0)

    def __str__(self):
        return f'fecha: {self.fecha} - nombre: {self.nombre} - descripcion: {self.descripcion} - nivel: {self.nivel} - numeros: {self.numeros} - ceros: {self.ceros} - progreso: {self.progreso} - movimientos: {self.movimientos}'
