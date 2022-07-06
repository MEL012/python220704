# DemoFormat.py

url = "http://ycampus.com/?page=" + str(1)
print(url)

print("--- 정렬 방식 미지정---")
for i in range(1, 6):
    print(i, "*", i, str(i*i))

print("--- 정렬 방식 지정1---")
for i in range(1, 6):
    print(i, "*", i, str(i*i).rjust(3))

print("--- 정렬 방식 지정2---")
for i in range(1, 6):
    print(i, "*", i, str(i*i).zfill(3))

print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(1500000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))