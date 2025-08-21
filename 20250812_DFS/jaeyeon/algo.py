
def dfs(current, dist):

    global max_dist
    if not node_list[current]:

        max_dist = max(max_dist, dist)

        print(max_dist)
        return

    for now, now_dist in node_list[current]:
        print(node_list[current])

        dfs(now, dist+now_dist)

        print(node_list[current])


# 정점의 개수
n = int(input())

# 노드 리스트
node_list = [[] for _ in range(n+1)]

# 노드 입력
for i in range(n):
    nodes = list(map(int,input().split()))

    node1 = nodes[0]

    # 부모 노드에 자식 노드들 삽입
    for j in range(1,len(nodes)-1,2):

        node_list[node1].append((nodes[j],nodes[j+1]))

print(node_list)

# 방문 확인,, 필요한가
visited = [False]*(n+1)

# 트리의 지름
max_dist = 0

# 현재 노드, 거리
dfs(1,0)


# 출력
print(max_dist)