def checkvalue(num):
    a = int(num**0.5)
    if num == 1:
        return False
    else:
        for i in range(2, a+1):
            if num % i == 0:
                return False
        return True

lst = []

for i in list(range(2, 246912)): #제한 1 <= n <= 123,456
    if checkvalue(i):
        lst.append(i)

while True:
    M = int(input())
    cnt = 0
    if M == 0:
        break
    for i in lst:
        if M < i <= M*2:
            cnt += 1
    print(cnt)