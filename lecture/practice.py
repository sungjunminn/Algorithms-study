import time
start_time = time.time()

def solution(L, x):
    answer = L
    for i in L:
        if i <= x:
            idx = L.index(i) + 1
    L.insert(idx, x)
    return answer

print(solution([20, 37, 58, 72, 91], 65))

end_time = time.time()
print("time :", end_time - start_time)