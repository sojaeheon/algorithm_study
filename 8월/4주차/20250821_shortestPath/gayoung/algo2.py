'''
    1~N 번까지 도시
    M개의 단방향
    최단거리가 K인 모든 도시들의 번호 출력
    자기 자신은 0
    도시 X로부터 출발하여 도달할 수 있는 모든 도시 중 -> 양수다. 다익스트라
    단방향 도로가 존재
    최단 거리가 K인 도시가 하나도 존재하지 않으면 -1
'''
import heapq, math


def dijkstra(adj_list, start):
    distances = {v: math.inf for v in nodes}
    distances[start] = 0
    # 힙큐 생성, 데이터 넣기
    heap = []
    heapq.heappush(heap, [0, start])

    # 방문 체크
    visit = set()
    visit.add(start)

    # 목표 정점까지 거리 탐색
    while heap:
        # 데이터 뽑아오기
        weight, now = heapq.heappop(heap)

        # 방문 확인
        if now in visit and distances[now] < weight: continue

        # 방문처리
        visit.add(now)

        # 거리 확인
        for next, dist in adj_list[now]:
            next_distances = dist + weight
            if next_distances < distances[next]:
                distances[next] = next_distances
                heapq.heappush(heap, [next_distances, next])
    return distances


# N: 도시의 개수 , M: 도로의 개수 , K: 거리 정보 , 출발 도시 X
N, M, K, X = map(int, input().split())
nodes = [i for i in range(N + 1)]

# 인접 리스트 생성
adj_list = {nodes[v]: [] for v in range(len(nodes))}
for _ in range(M):
    s, e = map(int, input().split())
    adj_list[s].append((e, 1))

result = dijkstra(adj_list, X)
for items in result.items():
    if items[1] == K:
        print(items[0])


