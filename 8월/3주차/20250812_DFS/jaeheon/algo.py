

# DFS로 가장 먼 노드와 거리 찾기
def dfs(start):
    visited = [False] * (n + 1)
    stack = [(start, 0)]
    far_node = start
    max_dist = 0

    while stack:
        node, dist = stack.pop()
        if visited[node]:
            continue
        visited[node] = True

        if dist > max_dist:
            max_dist = dist
            far_node = node

        for v, w in tree[node]:
            if not visited[v]:
                stack.append((v, dist + w))

    return far_node, max_dist

n = int(input())

tree = [[] for _ in range(n+1)]

# 입력값을 인접 리스트로 바꾸기
for _ in range(n):
  inp = list(map(int,input().strip().split()))
  idx = 1
  v1 = inp[0]
  while inp[idx] != -1:
    v2 = inp[idx]
    dis = inp[idx+1]
    idx+=2

    if (v2,dis) not in tree[v1]:
      tree[v1].append((v2,dis))
      tree[v2].append((v1,dis))


# 가장 멀리 있는 노드를 찾는다
u, _ = dfs(1)

# u에서 가장 먼 노드까지 거리 = 트리지름
_, distance = dfs(u)


print(distance)
