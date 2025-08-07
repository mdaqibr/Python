import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
print(x.strftime("%H:%M:%S %d %A %B %Y "))

# Create date object:
x = datetime.datetime(2020, 5, 17)
print(x)

# Learn strtime method:
x = datetime.datetime(2018, 6, 1)
print("-------")
print(x.strftime("%d %a %b %y %p"))
print("-------")
print(x.strftime("%H:%M:%S %d %A %B %Y "))
print("-------")

