# A decorator is a function that modifies the behavior of another function without changing its code.
# Use Cases
#   Logging
#   Authentication
#   Timing execution
#   Access control (permissions)


def tabrak_tabrak(original_function):
    def wrapper_function():
        print("Before the function runs")
        original_function()
        print("After the function runs")
    return wrapper_function

@tabrak_tabrak
def say_hello():
    print("Hello!")

@tabrak_tabrak
def bye_bye():
  print("Say bye..")

say_hello()
bye_bye()

# Decorator with Arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Aqib")