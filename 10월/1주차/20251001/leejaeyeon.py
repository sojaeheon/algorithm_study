'''
연구소

NxM 직사각형 
벽 3개 세워야 함
0은 빈 칸 , 1은 벽, 2는 바이러스

벽 3개 지정하는 함수

바이러스 퍼지는 함수

0 세기

'''
from itertools import combinations
import copy

def bfs():
    q = copy.deepcopy(virus)
    arr = copy.deepcopy(map_list)
    
    visited = set()

    while q:
        dx, dy = q.pop(0)
        visited.add((dx,dy))

        for i in range(4):
            nx,ny = dx+pos[i][0], dy + pos[i][1]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and (nx,ny) not in visited:
                arr[nx][ny] = 2
                visited.add((nx,ny))
                q.append((nx,ny))

    result = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                result += 1

    return result
        


    
pos = [(0,1),(0,-1), (1,0), (-1,0)]
n,m = map(int,input().split())

map_list = [list(map(int,input().split())) for _ in range(n)]

space = []
virus = []

for i in range(n):
    for j in range(m):
        if map_list[i][j] == 0:
            space.append((i,j))
        elif map_list[i][j] == 2:
            virus.append((i,j))

result = 0
for walls in combinations(space, 3):
    for i in range(3):
        map_list[walls[i][0]][walls[i][1]] = 1
    result = max(bfs(), result)

    for i in range(3):
        map_list[walls[i][0]][walls[i][1]] = 0
    
print(result)