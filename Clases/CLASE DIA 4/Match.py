cliente = {'nombre':'Arturo',
           'edad': 35,
           'ocupacion': 'Desarrollador'}

pelicula = {'titulo': 'Matrix',
            'ficha_tecnica': {'protagonista':'Keanu Reeves',
                              'director':'Lana y Willy Wachowski'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad' : edad,
              'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case{'titulo':titulo,
             'ficha_tecnica': {'protagonista': protagonista,
                              'director':director }}:
            print("Esto es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto")