def dfs(depth):
    if depth == m:
        print(*ans)
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        ans.append(i)

        dfs(depth + 1)

        visited[i] = False
        ans.pop()

# 정수, 길이
n, m = map(int, input().split())
visited = [False] * (n + 1)
ans = []
dfs(0)
