data = input()
column = int(chr(ord(data[0]) - 48))
row = int(data[1])

# 방향
dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]
count = 0

for i in range(8):
    nx = column + dx[i]
    ny = row + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx > 0 and ny > 0 and nx <= 8 and ny <= 8:
        count += 1

print(count)

