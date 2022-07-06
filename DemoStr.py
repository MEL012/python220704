# DemoStr.py
import sys

# print(dir(str))

strA = "python is very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))
print(len(strB.encode()))
print(sys.getsizeof(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p", 7))

print(strA.startswith("python"))
print(strA.endswith("ful"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("MBC2580".isdecimal())
print("2580".isdecimal())

u = "<<< spam and ham >>>"
result = u.strip("<> ")
print(u)
print(result)
result = result.replace("spam", "spam egg")
print(result)
lst = result.split()
print(lst)
print(":)".join(lst))
print(strA.upper())
print(strA.lower())