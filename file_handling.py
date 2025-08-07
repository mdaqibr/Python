# file = open("sample.txt", "r")
# print(file.read())
# file.close()

# Using 'with' - Then you will not have to close the file.
print("Printing one line.....")
with open("sample.txt") as f:
  print(f.read()) # read entire file.
  print("\n-------------\n")
  print(f.read(5)) # read first 5 letters.
  print(f.readline()) # read one line only.
  print(f.readline())
  print(f.readline())
  print(f.readline())

print("\nUsing loop..............")
with open("sample.txt") as f:
  for x in f:
    print(x)
    
print("\nWriting into file...............")
with open("sample.txt", "a") as f:
  f.write("\nNow the file has more content!")

print("\nNow reading file after updating it..............")
with open("sample.txt") as f:
  print(f.read())
  
print("\nOverriding the content...........")
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

print("\nopen and read the file after the overwriting..............")
with open("demofile.txt") as f:
  print(f.read())
  
print("\nCreating new file..............")
try:
  f = open("sample.txt", "x")
  f.write("Added new line in the new file.")
except Exception as e:
  print("Error in file creating.", str(e))

print("\nDeleting the file.........")
import os
if os.path.exists("myfile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  
try:
  os.rmdir("myfolder") # Note: You can only remove empty folders.
except Exception as e:
  print("Folder not present.")