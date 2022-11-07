def solution(cost, x):
    count = 0
    for i in cost:
        count += x // i
        x %= i

    return 2**count

# print(solution([3, 4, 1], 8))
print(solution([19, 78, 27, 18, 20], 25))
