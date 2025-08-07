mylist = ["apple", "banana", "cherry"]
print(mylist)

list1 = ["abc", 34, True, 40, "male"]
print(list1)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist[0] = 'papaya'
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

print("List comprehension...")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits if "a" == x[0]]
print(newlist)
print(fruits)

print("Shorting...")

thislist = [100, 50, 65, 82, 23]
newL = thislist
newL.sort(reverse = False)
print(thislist)

def myfunc(n):
  # print(abs(n - 10))
  return abs(n - 10)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str)
thislist.reverse()
print(thislist)

print("Copying.......")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
mylist[0] = "Aqib"
print(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
mylist[0] = "NewVal"
print(mylist)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
mylist[0] = "Changed"
print(mylist)
print(thislist)

new_list = ["Aqib", 20, True, 10.0]
for i, j in enumerate(new_list):
  print(i,j)

print(new_list)


for x in range(10, 1, -2):
  print(x)

print("Karduu....")
new_list = ["apple", "banana", "cherry"]
list2 = new_list
list2[0] = "Karduuu.."
print(new_list)
