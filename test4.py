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


# You said increment restarts and carries nothing. That would be true if increment was a normal standalone function. But it's not. It was born inside counter, next to count.
# When counter() runs and returns increment, the increment function takes count with it. It carries the variable from the room it was born in.
# This is called a closure.
# Think of it like this:
# You grew up in a house with a fridge. You move out of the house. The house is gone. But you remember where the fridge was and you still have access to what was in it.
# increment moved out of counter. counter finished. But increment still holds a reference to count from that room.

# So what actually happens:
# pythonc = counter()

# counter() runs
# count = 0 created
# increment function created, it grabs a reference to count
# counter returns increment
# c now points to the increment function
# BUT count is NOT destroyed — increment is still holding onto it

# pythonprint(c())  # count becomes 1, returns 1
# print(c())  # count becomes 2, returns 2  
# print(c())  # count becomes 3, returns 3
# Same count variable. Persisting across calls. Because increment is keeping it alive.

# Diagram:
# c ----→ increment function
#            └── holds reference to → count (stays alive in memory)
# count survives because something still points to it. Python never destroys objects that still have something pointing to them.

# This is called a closure — a function that remembers the variables from the scope it was born in, even after that scope is gone.

#new changes