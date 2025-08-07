try:
  print(10)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  
print("\n")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("Final block.")