# db1.py
import sqlite3

# 메모리에서 작업
con = sqlite3.connect(":memory:")

# 커서객체를 리턴
cur = con.cursor()

# 데이터를 저장할 테이블 생성
cur.execute("CREATE TABLE PhoneBook (Name text, PhoneNum text);")

# 1건 입력
cur.execute("INSERT INTO PhoneBook values ('drick', '010-222');")

# 검색
cur.execute("SELECT * FROM PhoneBook;")
for row in cur:
    print(row)