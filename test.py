a = "hello"
b = a

print(id(a))
print(id(b))  # should be identical to id(a)

a = "world"

print(id(a))  # should be different now
print(id(b))  # should still be the old number