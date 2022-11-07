def solution(number, k):
    stack = [number[0]]
    count = 0

    for i in range(1, len(number)):
        if count == k:
            stack = stack + number[i:]
            break

        stack.append(number[i])
        if stack[-1] > stack[-2]:
            while(len(stack) != 1 and stack[-1] > stack[-2] and count < k):
                stack[-2], stack[-1] = stack[-1], stack[-2]
                stack.pop()
                count += 1
    return "".join(stack[:len(number)-k])
print(solution([3, 4, 1], 8))
print(solution([19, 78, 27, 18, 20], 25))