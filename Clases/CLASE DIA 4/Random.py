from random import *

aleatorio = randint(1,50)
print(aleatorio)

alea = random()
print(alea)

colores = ['azul', 'rojo', 'verde', 'amarillo']
pickcolors = choice(colores)
print(pickcolors)

numeros = list(range (5,50,5))
shuffle(numeros)
print(numeros)