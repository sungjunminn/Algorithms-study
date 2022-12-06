from collections import deque
n, m, v = map(int, input().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (n + 1) # dfs 방문기록
visited2 = [False] * (n + 1) # bfs 방문기록

def dfs(v):
    visited1[v] = True # 해당 노드 방문처리
    print(v, end=" ")
    for i in range(1, n + 1):
        if not visited1[i] and graph[v][i]: # 만약 i값을 방문하지 않았고, v와 연결되어 있다면
            dfs(i) # i값으로 dfs를 실행한다.

def bfs(v):
    queue = deque([v])
    visited2[v] = True # 해당 노드 방문처리
    while queue: # queue가 빌 때까지 돈다.
        v = queue.popleft() # 큐의 첫 번재 값을 꺼낸다.
        print(v, end=" ")
        for i in range(1, n + 1):
            if not visited2[i] and graph[v][i]: #만약 i값을 방문하지 않았고, v와 연결되어 있다면
                queue.append(i) # i값 추가
                visited2[i] = True # i값 방문처리


dfs(v)
print()
bfs(v)