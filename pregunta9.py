# GrafoNodirigido
import sys 
import math 
import heapq

class GrafoNoDirigido:
    def __init__(self):
        # Diccionario vertice: lista de tuplas (vertices,peso)
        self.vertices = {}
        self.cantidad_vertices = 0

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
            self.cantidad_vertices += 1
    
    def agregar_arista (self, vertice1, vertice2, peso):
        self.agregar_vertice(vertice1)
        self.agregar_vertice(vertice2)
        self.vertices[vertice1].append((vertice2,peso))
        self.vertices[vertice2].append((vertice1,peso))

    def cargar_desde_archivo(self, archivo):
        with open(archivo) as f:
            for linea in f:
                vertice1, vertice2, peso = linea.strip().split(',')
                self.agregar_arista(vertice1, vertice2, int(peso))
    
    def obtener_vertices(self):
        return self.vertices.keys()

    