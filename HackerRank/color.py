import os

def solution(cost, x):
    for i in range(len(cost)):
        if x == 1:
            yield [cost[i]]
        else:
            for next in solution(cost[i+1:], x-1):
                yield [cost[i]] + next

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
# 
#     cost_count  = int(input().strip())
#
#     cost = []
#
#     for _ in range(cost_count):
#         cost_item = int(input().strip())
#         cost.append(cost_item)
#
#     x = int(input().strip())
#
#     result = solution(cost, x)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

# for i in solution([3, 4, 1], 8):
#     print(i, end=" ")
#
#
print(solution([3, 4, 1], 8))