

def distance_calculate(start,end):
  
    stack = [start]
    dis_sum = 0

    while stack:
        current_node = stack.pop()
        visited[current_node] = False

        stack += graph[]
        
        

    




# 노드의 개수 n, 알고 싶은 노드 쌍의 개수 m
n, m = map(int,input().strip().split())

graph = []
visited = [True]*(n+1)

for _ in range(n-1):
    node1, node2, distance = map(int,input().strip().split())
    graph[node1][node2] = distance
    graph[node2][node1] = distance

for _ in range(m):
    start,end = map(int,input().split())
    distance_calculate(start,end)

