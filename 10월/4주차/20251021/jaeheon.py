import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 방향 (상, 하, 좌, 우)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * M for _ in range(N)]
answer = 0

# DFS 탐색 (깊이 4까지)
def dfs(x, y, depth, total):
    global answer
    if depth == 4:
        answer = max(answer, total)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False


# 'ㅗ', 'ㅜ', 'ㅏ', 'ㅓ' 모양 예외 처리
def check_extra(x, y):
    global answer
    # 중심 기준 4가지 'ㅗ' 모양
    extra_shapes = [
        [(0, 0), (0, 1), (0, -1), (-1, 0)],  # ㅗ
        [(0, 0), (0, 1), (0, -1), (1, 0)],   # ㅜ
        [(0, 0), (1, 0), (-1, 0), (0, 1)],   # ㅏ
        [(0, 0), (1, 0), (-1, 0), (0, -1)]   # ㅓ
    ]

    for shape in extra_shapes:
        valid = True
        s = 0
        for dx_, dy_ in shape:
            nx, ny = x + dx_, y + dy_
            if 0 <= nx < N and 0 <= ny < M:
                s += board[nx][ny]
            else:
                valid = False
                break
        if valid:
            answer = max(answer, s)


# 전체 탐색
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check_extra(i, j)

print(answer)
