a = 1000 - int(input())
change = [500, 100, 50, 10, 5, 1]
count = 0

for coin in change:
    count += a // coin
    a %= coin
print(count)