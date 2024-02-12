# USO DEL kwargs #

def suma(**kwargs):
    
    total = 0
    
    
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
        
    return total
        
        
print(suma(x=3, y=5, z=2))


def prueba(num1, num2, *args, **kwargs):
    
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')
    
    for arg in args:
        print(f'args = {arg}')
        
        
        
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        
args = [150,125,500,300]
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}

prueba(18,12, *args, **kwargs)