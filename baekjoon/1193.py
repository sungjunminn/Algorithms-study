n = int(input())

line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    x = n
    y = line - n + 1
elif line % 2 == 1:
    x = line - n + 1
    y = n

print(f'{x}/{y}')