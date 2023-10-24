from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Ingresa tu nombre por favor: ")

print(f"Bueno {nombre}, he pensado un numero entre 1 y 100\n tienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cual es el numero?: "))
    intentos += 1
    
    if estimado not in range(1,101):
        print("tu numero no se encuentra dentro del rango 1 al 100")
          
    if estimado < numero_secreto:
        print("Mi numero es mas alto")
        
    elif estimado > numero_secreto:
        print("Mi numero es mas bajo")
        
    else:
        print(f"Felicitaciones {nombre}! has adivinado en {intentos} intentos")
        break
if estimado != numero_secreto:
    print(f"Lo siento, se han agotados tus intentos. El numero secreto era {numero_secreto}")