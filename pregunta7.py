# Pregunta 7 
# Darth Vader le encarga desarrollar los algoritmos para organizar los Stormtrooper
# cumpliendo con las siguientes demandas:
# Deberá generar 2000 Stormtrooper siguiendo el formato de la imagen del primer ejecicio
# contemplando las siguientes legiones FL, TF, TK, CT, FN, FO y los dígitos generados de manera aleatoria;
import random
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

t = []
while len(t) <= 200:
    ob_1 = calificacion('FL',random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),'FL',random.randint(0,9))
    t.append(ob_1)

# Deberá cargar los Stormtrooper generados en dos tablas hash encadenadas, 
# en la primera se deberá agrupar de acuerdo con los tres últimos dígitos del 
# código y en la segunda a partir de las iniciales de la legión;


# Determinar si el Stormtrooper FN-2187 está cargado para poder quitarlo porque es un trai dor desertor. 

# Ahora obtenga todos los Stormtrooper terminados en 781 para asignarlos a una misión de asalto y a los terminados en 537 para una misión de exploración;

# ahora obtenga los Stormtrooper de la legión CT para que custodien a Darth Vader
# a una misión de exploración al planeta Hoth y los de la legión TF para una 
# misión de extermi nación a Endor.