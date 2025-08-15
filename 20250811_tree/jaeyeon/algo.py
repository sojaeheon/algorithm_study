from collections import deque

def bfs(start, end):
    # 방문여부, 큐에 시작 노드 삽입 (시작노드, 거리)
    visited = [False] * (N+1)
    queue = deque()
    queue.append((start,0))
    visited[start] = True       # 시작 노드 방문

    # 큐가 비어있을 때까지
    while queue:
        # 현재 노드, 현재 거리
        current_node , current_dist = queue.pop()

        if current_node == end: # 종료 조건
            return current_dist
        
        for next, dist in node_list[current_node]:  # 자식 노드 개수만큼
            if not visited[next]:
                visited[next] = True
                queue.append((next,current_dist+dist))  # 거리 추가

    return 0

# 노드 개수 , 노드 쌍의 개수
N, M = map(int, input().split())

# 연결된 노드 저장 리스트
node_list = [[] for _ in range(N+1)]

for i in range(N-1):
    # 연결된 노드와 거리 입력
    node1, node2, dist = map(int,input().split())

    # 서로의 노드에 저장
    node_list[node1].append((node2,dist))
    node_list[node2].append((node1,dist))

# 찾아야 할 노드 간 거리
for i in range(M):
    n1, n2 = map(int,input().split())

    print(bfs(n1,n2))