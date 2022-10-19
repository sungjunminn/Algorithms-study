T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    height = N % H
    width = N // H + 1
    if height == 0:
        width = N // H
        height = H
    print(f'{height*100+width}')