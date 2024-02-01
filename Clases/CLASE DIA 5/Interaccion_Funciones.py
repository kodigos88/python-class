from random import shuffle

# Primero se crea una lista inicial
palitos = ['-', '--', '---', '----']

# Segundo mezclar palitos

def mezclar(lista):
    shuffle(lista)
    return lista

# Tercero pedirle intento

def probar_suerte():
    intento = ''
    
    while intento not in ['1','2','3','4']:
        intento = input('Elige un numero del 1 al 4: ')
        
    return int(intento)


# Cuarto Comprobamos el intento

def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('Has perdido')
    else:
        print('Te has salvado')
    
    print(f'Te ha tocado {lista[intento - 1]}')
    
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)