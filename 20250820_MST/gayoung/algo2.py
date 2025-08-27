'''
    프림은 힙큐를 이용한다.
    하나의 정점을 선택해서 가중치가 작은 간선을 선택한다.
    최소 비용의 합 구하기
'''
import heapq
def prim(vertices):
    mst = []
    visit = set()
    start = vertices[1]
    heap = [(w,s,e) for e, w in edges[start]]
    heapq.heapify(heap)
    visit.add(start)

    while heap:
        weight, start, end = heapq.heappop(heap)
        if end in visit: continue

        visit.add(end)
        mst.append((start, end, weight))

        for next, weight in edges[end]:
            if next in visit: continue
            heapq.heappush(heap, (weight, end, next))
    return mst


# 컴퓨터 수, 간선 수
N = int(input())
M = int(input())

edges = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    edges[s].append((e, w))
    edges[e].append((s, w))

# 노드 기록
vertices = [v for v in range(N + 1)]
result = prim(vertices)

ans = 0
for lst in result:
    ans += lst[2]
print(ans)