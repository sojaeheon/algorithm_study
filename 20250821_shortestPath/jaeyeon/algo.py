import heapq, math

def dijkstra(graph, start):
    distances = {v: math.inf for v in graph}

    distances[start] = 0

    heap = []
    heapq.heappush(heap,[0,start])

    visited = set()

    while heap:
        dist, current = heapq.heappop(heap)

        if current in visited or distances[current] < dist: continue

        visited.add(current)

        for next, weight in graph[current]:
            next_distance = dist + weight

            if next_distance < distances[next]:
                distances[next] = next_distance
                heapq.heappush(heap, [next_distance, next])
    return distances

N, M = map(int,input().split())

adj_list = {v : [] for v in range(N+1)}

for i in range(M):
    n1 , n2, w = map(int,input().split())

    adj_list[n1].append((n2,w))
    adj_list[n2].append((n1,w))

result = dijkstra(adj_list,1)
print(result[N])