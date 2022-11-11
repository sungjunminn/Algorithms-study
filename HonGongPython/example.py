# 메모화 풀이
앉힐수있는최소사람수 = 2
앉힐수있는최대사람수 = 10
전체사람수 = 100
memo = {}  # 메모화 딕셔너리


def 문제(남은사람수, 앉힌사람수):
    # 다음과 같은 매개인자가 들어왔을때 메모에 있으면 꺼내쓰기 위해
    key = str([남은사람수, 앉힌사람수])

    # 탈출조건
    if key in memo:
        return memo[key]
    if 남은사람수 < 0:  # 1 인경우는 다음 트리로 넘어가면서 0 보다 작은 상태로 넘어감
        return 0
    if 남은사람수 == 0:
        return 1

    # 재귀함수
    counter = 0
    for i in range(앉힌사람수, 앉힐수있는최대사람수+1):
        counter += 문제(남은사람수-i, i)
    # 메모화
    memo[key] = counter

    return counter


print(문제(전체사람수, 앉힐수있는최소사람수))

