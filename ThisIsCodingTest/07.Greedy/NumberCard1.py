N, M = map(int, input().split())
result = []
for lst in range(N):
    cards = list(map(int, input().split()))
    result.append(min(cards))

print(max(result))




