mi_set = set((1,2,3,4,5))
print(len(mi_set))
print(type(mi_set))
print(mi_set)
print(2 in mi_set)

# UNION DE SETS #

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

# USANDO VARIOS METODOS #

c1 = {1,2,3}
c1.add(4)
print(c1)