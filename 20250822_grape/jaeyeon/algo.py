from itertools import combinations
from collections import deque
import copy

def bfs(walls):
    # deepcopy를 통해 matrix를 복사함 
    tmp = copy.deepcopy(matrix)

    # 조합을 통해 고른 3개의 빈 곳을 벽으로 바꿈
    for x,y in walls:
        tmp[x][y] = 1
    
    # 바이러스 좌표 저장
    q = deque(virus)

    # 큐가 빌 때까지
    while q:
        x,y = q.popleft()

        # 4방향 순회
        for i in range(4):
            nx, ny = x + pos[i][0] , y + pos[i][1]
            if 0 <= nx < N and 0 <= ny <M  and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2     # 0이라면 2로 바꿔줌 (바이러스 침투)
                q.append((nx,ny))   # 해당 좌표 큐에 추가

    safe = sum(i.count(0) for i in tmp) # 안전지대(0인 경우) 개수 세기
    return safe


pos = [(0,1),(0,-1),(1,0),(-1,0)]

# 입력
N,M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

wall = []  # 벽 좌표 리스트
virus = []  # 바이러스 좌표 리스트
result = 0      # 결과 저장
# 2차원 행렬 순회
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:       # 벽을 만들 수 있는 곳일 때
            wall.append((i,j))
        elif matrix[i][j] == 2:     # 바이러스가 존재하는 곳
            virus.append((i,j))

# 조합을 통해 0인 좌표를 골라 bfs로 데려감
for walls in combinations(wall,3): 
    result = max(result, bfs(walls)) # 최대 안전지대 개수 세기

print(result)