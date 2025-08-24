from collections import deque

def bfs():
    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()

        # 4방향 순회
        for i in range(4):
            nx, ny = x + pos[i][0], y + pos[i][1]
            # 배열 내에 있고 해당 값이 0일 때 (아직 안다녀간 곳일 때)
            if 0<= nx <m and 0 <= ny < n and tomato_list[nx][ny] == 0:
                tomato_list[nx][ny] = tomato_list[x][y] +1
                queue.append((nx,ny))

        
        
# 방향 및 입력
pos = [(0,1),(0,-1),(-1,0),(1,0)]
n, m = map(int,input().split())

tomato_list = [list(map(int,input().split())) for _ in range(m)]

# 큐
queue = deque()

# 2차원 배열 순회하며 1인 경우 큐에 추가
for row in range(m):
    for col in range(n):
        if tomato_list[row][col]==1:
            queue.append((row,col))

# bfs 시작 (큐를 가지고)
bfs()


# 최대 일수
max_day = 0
# 모든 토마토가 익었는지 확인
check = True

# 배열 순회 -> 안익은 토마토가 있는지 + 최대 일수 기록
for r in range(m):
    for c in range(n):
        if tomato_list[r][c] == 0:
            check = False
        max_day = max(max_day, tomato_list[r][c])

# 안익은 토마토 있으면 
if not check :
    print(-1)
# 다 익었다면 최대 일수 반환 -> 시작 날짜를 1로 시작했으므로 최대 일수 -1
else:
    print(max_day-1)