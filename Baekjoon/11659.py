import sys

N, M = map(int, input().split())
data = list(map(int, sys.stdin.readline().split()))

sum_value = 0
prefix_sum = [0]

for k in data:
    sum_value += k
    prefix_sum.append(sum_value)

for prefix in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i - 1])




