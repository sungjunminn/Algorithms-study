def solution(cost, x):
    count = 0
    if sum(cost) <= x:
        for i in cost:
            count += x // i
            x %= i
    else:
        for i in cost:
            count += x // i
            x %= i
            count = 2**count
    return count

# print(solution([3, 4, 1], 8))
print(solution([19, 78, 27, 18, 20], 25))