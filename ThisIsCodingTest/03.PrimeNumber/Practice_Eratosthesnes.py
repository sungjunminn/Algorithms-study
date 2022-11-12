def Eratosthesnes(n):
    sieve = [False, False] + [True] * (n - 1)
    count = 0
    for i in range(2, n + 1):
        if sieve[i]:
            count += 1
        for j in range(i * 2, n + 1, i):
            sieve[j] = False
    return count
print(Eratosthesnes(100))