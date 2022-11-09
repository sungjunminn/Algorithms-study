M = int(input())
N = int(input())

sosu = []
for num in range(M,N+1):
    error = 0
    if num > 1:
        for k in range(2, num):   # 2부터 n-1까지
            if num % k == 0:
                error += 1   # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
                break
        if error == 0:
            sosu.append(num) # error가 없으면 소수에 추가

if len(sosu) > 0:   #소수의 개수가 1개 이상일 때
    print(sum(sosu))
    print(min(sosu))
else:   #소수가 없으면
    print(-1)