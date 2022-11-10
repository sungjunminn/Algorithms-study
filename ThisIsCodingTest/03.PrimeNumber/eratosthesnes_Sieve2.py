import time

n = 100
sieve = [False, False] + [True] * (n - 1)
primes = []
for i in range(2, n + 1):
    if (sieve[i]):
        primes.append(i)
    for j in range(i * 2, n+ 1, i):
        sieve[j] = False

print(sieve)
print(primes)
print(len(primes))

# 함수로 구현
def countPrimes2(n):
    sieve = [False, False] + [True] * (n - 1)
    count = 0
    for i in range(2, n + 1):
        if (sieve[i]):
            count += 1
        for j in range(i * 2, n + 1, i):
            sieve[j] = False
    return count

n = 1000000
start = time.time()
print(countPrimes2(n))
elapsed = time.time() - start
print(elapsed, '초')
print(elapsed/60, '분')
print(elapsed/60/60, '시간')
