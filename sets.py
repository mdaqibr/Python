thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry", "apple", True, 1, 2}

print(thisset)
print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


thisset.add("orange")

print(thisset)

thisset = {"simple"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) # Merge
print(thisset)

# Note: If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}

if "bananda" in thisset:
  thisset.remove("banana")

# Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("banadna")
print(thisset)

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
x = thisset.pop()
print("Removed element is: ", x)
thisset.clear()
print(thisset)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
set4 = set1 | set2
print(set3)
print(set4)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
print("Joiniing a set with a tuple:")
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# Note: Both union() and update() will exclude any duplicate items.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

print("Joining set1 and set2, but keep only the duplicates:")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

print("Using & to join two sets:")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

print("intersection_update()")
set1.intersection_update(set2)

print(set1)
# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

# __________
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

print("difference()")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

print("\nUsing '-' instead of difference() to get the same result.")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)
# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

print("Using symmetric_difference().")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)