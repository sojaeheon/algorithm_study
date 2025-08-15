
def dfs(current, dist):

    global max_dist
    if node_list[current] == []:

        max_dist = max(max_dist, dist)

        print(max_dist)
        return

    for i in range(len(node_list[current])):

        if node_list[current]:
            n = node_list[current].pop()
        print(node_list[current])

        dfs(n[0], dist+n[1])

        print(node_list[current])

n = int(input())

node_list = [[] for _ in range(n+1)]

for i in range(n):
    nodes = list(map(int,input().split()))

    node1 = nodes[0]

    for j in range(1,len(nodes)-1,2):

        node_list[node1].append((nodes[j],nodes[j+1]))



print(node_list)

visited = [False]*(n+1)

max_dist = 0

dfs(1,0)



print(max_dist)