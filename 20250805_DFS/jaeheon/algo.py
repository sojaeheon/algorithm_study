
n = int(input())
picture = [list(input().strip()) for _ in range(n)]

# 방문 여부 배열
visited_normal = [[True]*n for _ in range(n)]
visited_unusual = [[True]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 일반인
def dfs_normal(x,y,color):
    stack = []
    stack.append((x,y))
    visited_normal[x][y] == False

    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                if visited_normal[nx][ny] and picture[nx][ny] == color:
                    visited_normal[nx][ny] = False
                    stack.append((nx,ny))


def dfs_unusual(x,y,color):
    stack = []
    stack.append((x,y))
    visited_unusual[x][y] == False

    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                if visited_unusual[nx][ny]:
                    if (color in 'RG' and picture[nx][ny] in 'RG') or picture[nx][ny] == color:
                        visited_unusual[nx][ny] = False
                        stack.append((nx,ny))
    
        
# 장애인

# 각각의 영역 수 세기
normal_count = 0
unusual_count = 0

for i in range(n):
    for j in range(n):
        if visited_normal[i][j]:
            dfs_normal(i, j, picture[i][j])
            normal_count += 1

        if visited_unusual[i][j]:
            dfs_unusual(i, j, picture[i][j])
            unusual_count += 1

print(normal_count, unusual_count)
