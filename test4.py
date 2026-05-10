def counter():
    count = 0
    def increment():
        count += 1 
        return count
    return increment

c = counter()
print(c())
print(c())
print(c())