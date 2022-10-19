M, N = map(int, input().split())

for num in range(M,N+1):
    if num == 1:
        continue
    for k in range(2, int(num**0.5)+1): #제곱근까지만 나누기
        if num % k == 0:
            break
    else:
        print(num)