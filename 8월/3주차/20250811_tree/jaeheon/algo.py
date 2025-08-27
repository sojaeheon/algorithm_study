

# 거리 탐색 함수
def distance_calculate(start, end, distance):
    if start == end:
        print(distance)
        return True

    visited[start] = False
    for node, w in graph[start]:
        if visited[node]:
            if distance_calculate(node, end, distance + w):
                # 백트래킹
                visited[start] = True
                return True

    # 백트래킹
    visited[start] = True
    return False


# 노드의 개수 n, 알고 싶은 노드 쌍의 개수 m
n, m = map(int, input().split())

# 인접 리스트로 변경
graph = [[] for _ in range(n + 1)]
visited = [True] * (n + 1)

# 간선 입력
for _ in range(n - 1):
    node1, node2, distance = map(int, input().split())
    graph[node1].append((node2, distance))
    graph[node2].append((node1, distance))

# 쿼리 입력 & 탐색 실행
for _ in range(m):
    start, end = map(int, input().split())
    distance_calculate(start, end, 0)
