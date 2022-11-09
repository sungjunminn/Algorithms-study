from collections import Counter

counter = Counter(['red', 'blue', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'가 등장한 횟수 출력
print(counter['red']) # 'red'가 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 변환

