msg = 'Hello, Aqib'

print(msg[0])

for ms in msg:
  if(ms == 'H'):
    print(ms)
  else:
    print("Do nothing")
    break

word = "Aqib"
if word in msg:
  print(word, "word is present.")
else:
  print(word, "is present.")
  
print(msg.upper())
print(msg.lower())
print(msg.strip())

print(msg.replace("Hello", "Good morning"))

print(msg)

print(msg.split(','))

print(f"My name is Aqib and I am {20} years old.")