#Práctica Operadores Lógicos 1 Crea tres variables (num1 ,  num2 y num3):

    #Dentro de num1, almacena el valor 36

    #Dentro de num2, almacena el resultado de la operación 72/2

    #Dentro de num3, almacena el valor 48

# Verifica si num1 es mayor que num2, y menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.

num1 = 36
num2 = 72/2
num3 = 48

mi_bool = (num1 > num2 < num3)

print(mi_bool)

# USANDO OPERADOR AND #
my_bool = 4 < 5 and (5 == 2+3)
print(my_bool)

# USANDO OPERADOR OR #

n1 = 1 == 10 or 3 == 3
print(type(n1))
print(n1)

texto = 'Esta frase es breve'
encontrar = ('frase' in texto) and ('breve' in texto)
print(encontrar)

# USANDO OPERADOR NOT #

c1 = not ('a' != 'a')
print(c1)