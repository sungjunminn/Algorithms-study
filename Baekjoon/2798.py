import itertools

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0

for number in itertools.combinations(numbers, 3):
    if result < sum(number) <= m:
        result = sum(number)

print(result)
