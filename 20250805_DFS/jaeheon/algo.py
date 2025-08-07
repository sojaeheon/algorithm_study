
# 동서남북을 탐색할 때 쓸 dx,dy변수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 일반인이 보는 그림 함수
def dfs_normal(x,y,color):
    # 다음 방문할 값을 저장할 stack 변수
    stack = []
    # 현재 값을 stack에 넣고 방문처리
    stack.append((x,y))
    visited_normal[x][y] == False

    # stack이 있는 동안 반복
    while stack:
        # 현재 위치
        cx, cy = stack.pop()
        # 동서남북 탐방
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 동서남북이 범위안에 있고
            if 0<=nx<n and 0<=ny<n:
                # 방문하지 않았고 다음 컬러가 현재 컬러랑 같으면
                if visited_normal[nx][ny] and picture[nx][ny] == color:
                    # 방문처리하고 다음 위치로 이동
                    visited_normal[nx][ny] = False
                    stack.append((nx,ny))

# 적록색약이 보는 그림 함수
def dfs_unusual(x,y,color):
    # 다음 방문할 값을 저장할 stack 변수
    stack = []
    # 현재 값을 stack에 넣고 방문처리
    stack.append((x,y))
    visited_unusual[x][y] == False

    # stack이 있는 동안 반복
    while stack:
        # 현재 위치
        cx, cy = stack.pop()
        # 동서남북 탐방
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # 동서남북이 범위안에 있고
            if 0<=nx<n and 0<=ny<n:
                # 방문하지 않았다면
                if visited_unusual[nx][ny]:
                    # 그리고 적록색약은 R과 G를 같은색으로 보기때문에 color가 RG고 다음 위치가 RG이면 같은 처리, 아니면 따로 처리
                    if (color in 'RG' and picture[nx][ny] in 'RG') or picture[nx][ny] == color:
                        visited_unusual[nx][ny] = False
                        stack.append((nx,ny))

n = int(input())
picture = [list(input().strip()) for _ in range(n)]

# 방문 여부 배열
visited_normal = [[True]*n for _ in range(n)]
visited_unusual = [[True]*n for _ in range(n)]
        
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
