# a = "hello"
# a.replace("hello", "world")
# print(a)
#Strings are immutable. .replace() cannot modify the original object. It creates a brand new string and returns it. But you threw that new string away by not storing it.
a = "hello"
a = a.replace("hello", "world")  # store the new string back
print(a)  # "world"
# This is mutability in action again. List .append() modifies in place. String .replace() returns a new object. Two completely different behaviors.
