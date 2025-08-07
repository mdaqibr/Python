# Iterator with tuple:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# Iterator with string:
sentence = "My name is Aqib"
iterable_str = iter(sentence)
print(next(iterable_str))
print(next(iterable_str))

# Create a custom iterator:
class MyNumber:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
  
myclass = MyNumber()

myiter = iter(myclass)

for x in myiter:
  print(x)

