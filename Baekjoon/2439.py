a = int(input())
b = 0
for i in range(a):
    a -= 1
    b += 1
    print(" "*a+"*"*b)