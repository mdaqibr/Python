def my_generator():
    yield "Hello G!"
    yield 2
    yield 3

gen = my_generator()
print(gen)
for val in gen:
    print(val)

# Example: Fibonacci Generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(5):
    print(next(fib))
    
# Generator Expression
  # Just like list comprehensions but using ():
squares = (x * x for x in range(5))
for s in squares:
    print(s)