def solution(x, y, z):
    k = 0
    for i in range(z):
        k += 1
    if x > y:
        k = x
    elif x <= y:
        k = k + 1

    return k

print(solution(4, 4, 4))