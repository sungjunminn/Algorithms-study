a = int(input())

for i in range(a):
    ls = list(map(int,input().split()))
    avg = sum(ls[1:])/ls[0]

    cnt = 0
    for j in ls[1:]:
        if j > avg:
            cnt += 1

    per = (cnt/ls[0])*100
    print('%.3f' %per + '%')