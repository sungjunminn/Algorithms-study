N = int(input())
N_input = list(map(int, input()))
result = 0
for i in range(len(N_input)):
    result += N_input[i]
print(result)