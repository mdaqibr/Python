import module_example as md
from module_example import job

print(md.APP_NAME)
md.welcome("Aqib")
print(md.person1["age"])

print(job)

# Built-in modules:
import platform

x = platform.system()
print(x)

x = dir(platform)
# print(x)