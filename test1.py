a = (1, 2, 3)
b = a
print(id(a) == id(b))

a = (4, 5, 6)
print(id(a) == id(b))