import math
import time

def isPrime2(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

def countPrimes(n):
    count = 0
    for i in range(2, n +1):
        if (isPrime2(i)):
            count += 1
    return count


n = 1000000
start = time.time()
m = countPrimes(n)
print(n, '이하의 소수는', m, '개 입니다.')
elapsed = time.time() - start
print(elapsed, '초')
print(elapsed/60, '분')
print(elapsed/60/60, '시간')