import sys

"""
4 5
00110
00011
11111
00000
"""

N, M = list(map(int, sys.stdin.readline().split()))

input_data = []
for _ in range(N):
    input_data.append(list(map(int, list(sys.stdin.readline().split()[0]))))

result = 0
visited = [[False]*M for _ in range(N)]
stack = []

def dfs(graph, n, m):
    visited[n][m] = True
    if n != 0:
        if graph[n-1][m] == 0 and not visited[n-1][m]:
            stack.append((n-1, m))
    if n + 1 < N:
        if graph[n+1][m] == 0 and not visited[n+1][m]:
            stack.append((n+1, m))
    if m != 0:
        if graph[n][m-1] == 0 and not visited[n][m-1]:
            stack.append((n, m-1))
    if m + 1 < M:
        if graph[n][m+1] == 0 and not visited[n][m+1]:
            stack.append((n, m+1))

    while len(stack) > 0:
        next_n, next_m = stack.pop()
        dfs(graph, next_n, next_m)


for n in range(N):
    for m in range(M):
        if input_data[n][m] == 1 or visited[n][m]:
            continue
        else:
            dfs(input_data, n, m)
            result += 1

print(result)


