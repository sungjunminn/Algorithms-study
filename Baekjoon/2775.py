T = int(input())

for i in range(T):
    k = int(input()) #층
    n = int(input()) #호
    cnt = [x for x in range(1, n+1)]
    for x in range(k):
        for y in range(1, n):
            cnt[y] += cnt[y-1]
    print(cnt[-1])