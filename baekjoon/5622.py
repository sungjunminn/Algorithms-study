alphabet = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
cnt = 0

for i in range(len(alphabet)):
    for j in dial:
        if alphabet[i] in j:
            cnt += dial.index(j)+3

print(cnt)