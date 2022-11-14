import itertools

while True:
    k, *S = map(int, input().split())
    S.sort()
    if k == 0:
        break
    for result in itertools.combinations(S, 6):
        print(' '.join(map(str, result)))
    print()
