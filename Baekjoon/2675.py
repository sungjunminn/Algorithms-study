S = int(input())
for i in range(S):
    num, t = input().split()
    text = ''
    for i in t:
        text += int(num) * i
    print(text)