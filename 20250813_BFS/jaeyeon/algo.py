from collections import deque

def bfs(col,row):
    global depth

    queue = deque()
    queue.append((col,row))
    visited = [[False] * (n+1) for _ in range(m)]
    
    while queue:
        current = queue.pop()
        if current == -1:
            return
        


pos = [(0,1),(0,-1),(-1,0),(1,0)]
n, m = map(int,input().split())

tomato_list = [list(map(int,input().split())) for _ in range(m)]

red_tomato = []
depth = 0

for row in range(n):
    for col in range(m):
        if tomato_list[col][row]==1:
            red_tomato.append((col,row))