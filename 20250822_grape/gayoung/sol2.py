dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, 1, 0, -1]

w, h = map(int, input().split())
while w != 0 and h != 0:
    arr = [list(map(int, input().split())) for _ in range(h)]
    # 방문 기록
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    stack = []
    # 시작 좌표 구하기 : 방문하지 않은 땅 찾기 = 새로운 땅 찾기
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                cnt += 1
                stack.append((i, j))
                visited[i][j] = True
                # 탐색하기
                while stack:
                    cr, cc = stack.pop()
                    for dr in range(8):
                        nr, nc = cr + dx[dr], cc + dy[dr]
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and arr[nr][nc]:
                            stack.append((nr, nc))
                            visited[nr][nc] = True
    print(cnt)
    w, h = map(int, input().split())
