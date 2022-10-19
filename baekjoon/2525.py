a,b = map(int, input().split())
c = int(input())

h = (b+c)//60
m = (b+c)%60

if b+c >= 60:
    if a+h >= 24:
        a = a - 24
    print(a + h , m)
else:
    if a >= 24:
        a = a - 24
    print(a, b+c)