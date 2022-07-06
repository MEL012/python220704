# DemoFile.py

# 파일 쓰기

f = open("C:\\work\\python220704\\demo.txt", "wt")

f.write("첫번째\n두번째\n세번째라인\n")
f.close()

print("C:/work/python220704/demo.txt")

# raw string notation(날것 그대로 가공안함) C#(@)
print(r"C:\work\python220704\demo.txt")

# 파일 읽기
f = open("C:\\work\\python220704\\demo.txt", "rt")
result = f.read()
print(result)

# 파일 포인터의 위치
print(f.tell())

# 다시 처음으로 이동(리셋)
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")

# 리스트로 출력
f.seek(0)
lst = f.readlines()
print(lst)

f.close()
print(f.closed)

# 기존 파일에 첨부하기
# with 키워드를 같이 쓰는 경우
with open("C:\\work\\python220704\\demo.txt", "a+") as f:
    f.write("새로운 데이터\n")