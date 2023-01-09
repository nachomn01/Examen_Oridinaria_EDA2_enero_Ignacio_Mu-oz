# Pregunta 6 
mochila2 = []
precio = [103, 60, 70, 5, 15] 
pesos = [12, 23, 11, 15, 7]
peso_maximo = 100
peso_total = 0 
for i in pesos:
    peso_total += i
print(f'El precio total es de {peso_total}')
# Podemos apreciar como peso_total es == 68 < 100
precio_total =0
if peso_total <= 100:
    for i in precio:
        precio_total += i
print(f'El precio total es de {precio_total} euros')