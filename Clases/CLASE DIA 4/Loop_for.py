lista = ['Arturo', 'Pablo', 'Luis', 'Julia', 'Fede']

for nombre in lista:
    if nombre.startswith('L'):
        print(nombre)
    else:
        print('Nombre que no comienza con L: ')
        
        
numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)


palabra = 'python'
for letra in palabra:
    print(letra)
    
dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}

for item in dic.items():
    print(item)
    
    
"""Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.

Por ejemplo: "Hola María"

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]"""

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
    print(f"Hola {alumno}")