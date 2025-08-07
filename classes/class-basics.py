class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
  # It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:

  def __init__(self, name, age):
    self.name = name
    self.age = age
    # print(self)
  
  def __str__(self):
    return f"{self.name}({self.age})"
  
  def get_name(self):
    return self.name
  
  def welcome(self):
    print(f"Welcome {self.name}!!")

class Student(Person):
  # Dundar, special, magic method (__init__):
  def __init__(self, name, age, subjects):
    super().__init__(name, age)
    self.subjects = subjects
  
  def welcome(self):
    super().welcome()
    # print(f"Welcome {self.name}, Happy to see you!!")

# class Girls(Student):
#   def __init__(self, colors):
#     self.colors = colors

# class Boys(Student):
#   def __init__(self, sports):
#     self.sports = sports

p1 = Person("John", 36)
print("Person Name: ", p1.get_name())

s1 = Student("Aqib", 20, ["Math", "Science", "SST", "Urdu"])
print("Student Name: ", s1.get_name(), "Subjects: ", s1.subjects)
print(s1.welcome())

# g1 = Girls("Sharah", 19)
# print("Girl name: ", g1.get_name())
# print("Fav colors:")

# b1 = Boys("Sarthak", 23)
# print("Boy name: ", b1.get_name())