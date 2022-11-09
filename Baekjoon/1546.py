a = int(input())
b = list(map(int, input().split()))
maxb = max(b)
ls = []

for i in b:
    ls.append(i/maxb *100)
avg = sum(ls)/a
print(avg)