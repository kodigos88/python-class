nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,33]
ciudades = ['Lima', 'Madrid', 'Argentina']

combinados = list(zip(nombres,edades,ciudades))

print(combinados)


for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")