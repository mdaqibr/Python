def my_function():
  print("Hello from a function")

my_function()

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def get_name(name, title = "Md"):
  print("Name with title: ", title, name)
  
get_name("Aqib")
get_name("Arshad", "Ghazi")
get_name("Prince", "Bharadwaj")

def get_car_colors(*args):
  for idx, val in enumerate(args):
    print(idx, ".", val)
  
get_car_colors("red", "blue", "marron", "black", "white")

def get_square(value):
  return value ** 2

squar = get_square(8)
print(squar)

def wow():
  pass

wow()

def outer():
    msg = 1
    def inner():
        nonlocal msg  # Tell Python: use the enclosing msg!
        msg += 1      # Increment properly
        print(msg)
    return inner

f = outer()
f()  # 2
f()  # 3
f()  # 4