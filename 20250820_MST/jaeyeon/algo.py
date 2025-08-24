import heapq

def prim(start_node, V, adj_list):
    visited = {start_node}

    min_heap = [(w,start_node,e) for e,w in adj_list[start_node]]

    heapq.heapify(min_heap)

    min_cost = 0

    while min_heap:
        weight,start, end = heapq.heappop(min_heap)

        if end in visited:
            continue

        visited.add(end)
        min_cost += weight


        if len(visited) == V:
            break

        for next_node, next_weight in adj_list[end]:
            if next_node not in visited:
                heapq.heappush(min_heap, (next_weight, end, next_node))

    return min_cost
V, E = map(int,input().split())

adj_list = {v : [] for v in range(V+1)}


for i in range(E):
    n1,n2,w = map(int,input().split())

    adj_list[n1].append((n2,w))
    adj_list[n2].append((n1,w))

result = prim(1,V,adj_list)

print(result)