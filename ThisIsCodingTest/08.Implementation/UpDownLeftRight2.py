N = int(input())
plans = list(map(str, input().split()))
X, Y = 1, 1

# 왼, 오, 위, 아래
for i in plans:
    if i == 'L' and Y > 1:
        Y -= 1
    elif i == 'R' and Y < N:
        Y += 1
    elif i == 'U' and X > 1:
        X -= 1
    elif i == 'D' and X < N:
        X += 1

print(X, Y)
