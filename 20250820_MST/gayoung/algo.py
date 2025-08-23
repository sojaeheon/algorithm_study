'''
    정점의 개수 V , 간선의 개수 E ,
    A, B, C , C는 음수 가능 : 프림
'''
import heapq, sys
input = sys.stdin.readline


def solve(edges):
    mst = []
    visit = set()
    start = nodes[1]
    heap = [(w, s, e) for e, w in edges[start]]
    heapq.heapify(heap)
    visit.add(start)
    while heap:
        weight, start, end = heapq.heappop(heap)
        if end in visit: continue

        visit.add(end)
        mst.append((start, end, weight))
        for next, dist in edges[end]:
            if next in visit: True
            heapq.heappush(heap, (dist, end, next))
    return mst


V, E = map(int, input().split())
nodes = [v for v in range(V + 1)]

edges = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    edges[s].append((e, w))
    edges[e].append((s, w))

result = solve(edges)

ans = 0
for num in result:
    ans += num[2]
print(ans)
