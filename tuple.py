new_tuple = ("Aqib", 20, True, 100.00)
print(new_tuple)

# new_tuple[0] = "Abu Nasar" // You cannot change the tuple once it created, it in unchangeable.
# print(new_tuple)

print(type(new_tuple))

tuple_2 = tuple("Aqib")
print(type(tuple_2))

thistuple = ("guava", "apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("Karduu..")
print(thistuple[-4:-1])

fruits = ("apple", "mango", "papaya", "apple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

fruits = ("apple", "banana", "cherry")
news = fruits
mytuple = fruits * 2
print(mytuple)

for x, c in enumerate(mytuple):
  print(x, c)

print(len(mytuple))