from collections import deque

def bfs(start_x, start_y):
    global max_dist
    # 방문 확인
    visited = [[False for _ in range(col)] for _ in range(row)] 

    # 큐에 시작 x, y, dist 삽입 
    queue = deque()
    queue.append((start_x, start_y, 0))
    visited[start_x][start_y] = True    # 방문

    # 현재 bfs에서의 최대 거리 확인
    current_max_dist = 0

    # 큐가 빌 때까지
    while(queue):
        x, y, dist = queue.popleft()
        current_max_dist = max(current_max_dist, dist)
        # 4방향 순회
        for i in range(4):
            nx, ny = x+pos[i][0] , y+pos[i][1]

            # 조건에 맞다면
            if 0<= nx < row and 0 <= ny < col and map_list[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny,dist+1))
                
    max_dist = max(max_dist, current_max_dist)
    return


# 상하좌우
pos = [(0,-1), (0,1), (1,0), (-1,0)]
# 최단 거리
max_dist = 0

# 입력
row, col = map(int,input().split())

map_list = list(input() for _ in range(row))

# 2차원 배열 순회
for r in range(row):
    for c in range(col):
        if map_list[r][c] == 'L':   # L이면 bfs 탐색 시작
            bfs(r,c)

print(max_dist)