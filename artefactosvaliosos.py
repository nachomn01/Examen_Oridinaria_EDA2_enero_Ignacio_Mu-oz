# Pregunta 4
class artefactosvaliosos():
    def __init__(self,peso, nombre, precio, fecha_de_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_de_caducidad = fecha_de_caducidad

    def __str__(self):
        return '{} de peso:{} cuyo precio es:{} y caduca el:{}'.format(self.nombre, self.peso, self.precio, self.fecha_de_caducidad)
    

ob_1 = artefactosvaliosos(123,'mesa',110, 'No caduca')
ob_2 = artefactosvaliosos(20,'lavadora',432, 'No caduca')
ob_3 = artefactosvaliosos(1,'filete',21, 'Marzo del año 2023')
print(ob_1)
print(ob_2)
print(ob_3)
l = []
l.append(ob_3)
l.append(ob_2)
l.append(ob_1)
for i in l:
    print(i)
