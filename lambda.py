# lambda arguments : expression

# Use lambda functions when an anonymous function is required for a short period of time.

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  print(n)
  return lambda a, b : (a + b) * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11, 11))
print(mytripler(11, 11))