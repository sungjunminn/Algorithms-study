N = int(input())
P = list(map(int,input().split()))
P.sort()
count = 0

for i in range(N):
    for j in range(i + 1):
        count += P[j]

print(count)