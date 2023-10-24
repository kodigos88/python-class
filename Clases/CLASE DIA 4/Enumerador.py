lista = ['a','b','c']


for item in enumerate(lista):
    print(item)
    
# LA SEGUNDA FORMA EN QUE SE PUEDE RESOLVER EL EJERCICIO ES:

for indice, item in enumerate(lista):
    print(indice, item)
    
mis_tuples = list(enumerate(lista))
print(mis_tuples)