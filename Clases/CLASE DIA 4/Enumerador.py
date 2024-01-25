lista = ['a','b','c']


for item in enumerate(lista):
    print(item)
    
# LA SEGUNDA FORMA EN QUE SE PUEDE RESOLVER EL EJERCICIO ES:

for indice, item in enumerate(lista):
    print(indice, item)
    
mis_tuples = list(enumerate(lista))
print(mis_tuples[1])

"""Imprime en pantalla frases como la siguiente:

'{nombre} se encuentra en el índice {indice}'

Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate().

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser iguales."""

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')