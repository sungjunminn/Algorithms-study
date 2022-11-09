n = int(input())

bee = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > bee :
    bee += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1
print(cnt)