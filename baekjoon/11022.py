import sys

num = int(input())
ls = 0
for i in range(num):
    ls += 1
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{ls}:", f"{a} + {b} =", a+b)