thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

# if key is not present then it will raise error:
print(thisdict["brand"])

# even if the key is not present, then it will return None.
print(thisdict.get("brand"))

# It cannot have the same key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))

print("Using the dict() to make dictionary()")
thisdict = dict(branch = "Ford", electric =  True, year = 1964, colors = ["red", "white", "blue"])
print(thisdict)

thisdict = dict(branch = "Ford", Branch = "NewBranch", electric =  True, year = 1964, colors = ["red", "white", "blue"])

# Get keys:
print(thisdict.keys())

# Get values:
print(thisdict.values())

# Update value:
thisdict["branch"] = "Fortuner"
print(thisdict)

x = thisdict.items()
thisdict["branch"] = "Hyudai"
thisdict.update({"branch": "Toyota" })
print(x)

print("\nRemoving element.....")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
thisdict.popitem()
print(thisdict)

print("del...........")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
# del thisdict # Delete the dictionary.

for x, y in thisdict.items():
  print(x, y)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# mydict = thisdict # If changes made in new dictionary then the old will also update.
# mydict = thisdict.copy() # New dict will created.
mydict = dict(thisdict) # New dict created.
mydict["model"] = "I7"
print(thisdict)
print(mydict)

print("\nNested dictionary........")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
# Access values:
print(myfamily["child1"]["name"])
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])