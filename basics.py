print("Hello Aqib.")

"""
Commented line
second line.
"""
# one line comment.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

name, age, title = "Md Aqib", 20, "He is software developer."
print(name, age, title)


if 5 > 2:
  print("Five is greater than 2.")
  
  
val = "awesome"

def myfunc():
  global val # val =  "fantastic"
  print("Python is " + val)

myfunc()

print("Python is " + val)

print(range(6))

a = "Hello, World!"
print(a[1])
