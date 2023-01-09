# Pregunta 1
class stormtrooper():
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango 
        print("El objeto se ha credo con éxito")
    
class calificacion(stormtrooper):
    def __init__(self, codigo_de_legion, ident_cohoerte, ident_siglo, ident_escuadra, num_troop, nombre_h,rango_h ):
        super().__init__(nombre_h,rango_h)
        self.codigo_de_legion = codigo_de_legion
        self.ident_cohoerte = ident_cohoerte
        self.ident_siglo = ident_siglo
        self.ident_escuadra = ident_escuadra
        self.num_troop = num_troop
list = []
a = stormtrooper('play', 12)
list.append(a)
b = stormtrooper('zumo',8)

def mostrar(list):
    for i in list:
        print("El elemento {} tiene como resultado del metodo calificacion {}".format(i.nombre,i.calificacion))





# Pregunta 3
class stormtrooper():
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango 
        print("El objeto se ha credo con éxito")
        
    def __str__(self):
        return '{} con rango {}'.format(self.nombre, self.rango)
    
l = []
strom_1 = stormtrooper('camiseta',4)
l.append(strom_1)
strom_2 = stormtrooper('chaqueta',7)
l.append(strom_2)
strom_3 = stormtrooper('sudadera',9)
l.append(strom_3)

def recorrer (l):
    for i in l:
        print ('{}').format(i.str)





# 4 -> Pregunta 5
mochila = []
def usar_la_fuerza(l):
    for i in l:
        contador = 0
        if i.nombre != 'sable de luz':
            contador +=1
            return usar_la_fuerza(l-1)
        else:
            print('Se ha encontrado un objeto denominado  sable de luz y por ello se para')
            break
 
# La idea es coger la función, si el nombre es == sable de luz se sale de la función 
# Si no es != sable de luz, la función vuelve a llamarse








