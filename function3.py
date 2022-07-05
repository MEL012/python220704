# function3.py

# 교집합 함수
def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

# 호출
print(intersect("HAM", "SPAM"))