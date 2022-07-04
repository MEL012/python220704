# DemoList.py

from turtle import color


strB = """이 문자열은
다중 라인으로
저장합니다."""

print(strB)

#list
colors = ["red", "blue", "green"]
print(len(colors))
print(colors[0])

for item in colors:
    print(item)

colors.append("white")
print(colors)
colors.append("pink")
print(colors)
colors.insert(1, "yellow")
print(colors)
colors += "red"
print(colors)
print(colors.pop())
print(colors.pop())
print(colors.pop())
print(colors)
colors.remove("red")
print(colors)
print(colors.index("blue"))
print(colors.count("blue"))
colors.sort()
print(colors)
colors.reverse()
print(colors)

print("="*100)

#보통 데이터의 묶음
print("---tupe---")
tp = (1,2,3)
print(len(tp))
print(tp[0])
print("id: %s, name: %s" % ("Kim", "김길동"))

print("---set---")
a = {1,2,3,3}
print(a)
b = {3,4,4,5}
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("---Type case---")
a = set((1,2,3))
print(type(a))
print(a)
b = list(a)
print(b)
b.append(4)
print(b)
