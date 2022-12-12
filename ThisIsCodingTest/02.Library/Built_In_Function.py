# sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# min()
result = min(7, 3, 5, 2)
print(result)

# max()
result = max(7, 3, 5, 2)
print(result)

# eval()
result = eval('(3 + 5) * 7')
print(result)

# 리스트 sorted()로 정렬하기
result = sorted([9, 1, 8, 5, 4])
print(result)
result = sorted([9, 1, 8, 5, 4], reverse = True)
print(result)

# key를 이용한 리스트 sorted()로 정렬하기
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result)
[('이순신', 75), ('아무개', 50), ('홍길동', 35)]

# sort() 함수를 이용한 리스트 정렬하기
data = [9, 1, 8, 5, 4]
data.sort()
print(data)

