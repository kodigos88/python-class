edad = 18
calificacion = 9

if edad < 18:
	print('Eres menor de edad')
	if calificacion >= 7:
		print('Aprobaste! ')
	else:
		print('No aprobaste')
else:
	print('Eres Adulto')
 

"""Utilizando las variables num1 y num2, que se alimentan con el input del usuario (tal como en el código ya proporcionado):

Crea una estructura de control de flujo que compare los valores de las variables, y arroje un resultado de acuerdo al caso:
    "num1 es mayor que num2"

    "num2 es mayor que num1"

    "num1 y num2 son iguales"

Debes mostrar en pantalla el valor de las variables ingresadas en lugar de num1 y num2.

"""

# SOLUCION #

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")