def suma(*args):
    total = 0
    
    for arg in args:
        total += arg
    return total

print(suma(3,4,5,8))


# SEGUNDA FORMA MAS RAPIDA Y MENOS LINEAS #

def suma (*args):
    
    return sum(args)

print(suma(2,4,2,2))