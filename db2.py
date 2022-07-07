# db1.py
import sqlite3

# 메모리에서 작업
con = sqlite3.connect("c:\\work\\python220704\\sample4.db")

# 커서객체를 리턴
cur = con.cursor()

# 데이터를 저장할 테이블 생성
cur.execute("CREATE TABLE PhoneBook (Name text, PhoneNum text);")

# 1건 입력
cur.execute("INSERT INTO PhoneBook values ('drick', '010-222');")

# 입력 파라미터 처리
name = "gildong"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

# 다중의 레코드 입력(2차원 배열, 행렬 데이터)
datalist = (("tom", "010-345"), ("dsp", "010-333"))
cur.executemany("INSERT INTO PhoneBook values (?, ?);", datalist)

# 검색
cur.execute("SELECT * FROM PhoneBook;")
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
print(cur.fetchall())

con.commit()