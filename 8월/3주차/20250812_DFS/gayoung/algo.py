# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# def dfs(row, col):
#     # 가지치기 : 이미 방문했으면
#     if visit[row][col]:
#         return
#
#     # 초기 설정
#     visit[row][col] = True
#
#     # 4방향 탐색
#     for dr in range(4):
#         nr, nc = row + dx[dr], col + dy[dr]
#         # 조건: 범위 내, 첫 방문,  1이여야 함
#         if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc] and arr[nr][nc]:
#             # 다음 탐색
#             dfs(nr, nc)
#
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# T = int(input())
# result = []
# for _ in range(T):
#     # M: 가로 길이 , N: 세로길이, K: 배추 개수
#     M, N, K = map(int, input().split())
#     arr = [[0] * M for _ in range(N)]
#     for _ in range(K):
#         c, r = map(int, input().split())
#         arr[r][c] = 1
#
#     # 초기 설정
#     cnt = 0
#     visit = [[False] * M for _ in range(N)]
#     # 시작 지점 정하기
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] and not visit[i][j]:
#                 dfs(i, j)
#                 cnt += 1
#     result.append(cnt)
# for re in result:
#     print(re)
'''
버전 2
'''

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
result = []
for _ in range(T):
    # M: 가로 길이 , N: 세로길이, K: 배추 개수
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1

    # 방문 기록 & 값 추가
    visit = [[False] * M for _ in range(N)]
    ans = 0
    # 시작 지점 찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visit[i][j]:
                # 방문처리, stack 넣기, 횟수 추가
                visit[i][j] = True
                stack = [(i, j)]
                cnt = 1

                while stack:
                    cr, cc = stack.pop()
                    # 4방향 탐색
                    for dr in range(4):
                        nr, nc = cr + dx[dr], cc + dy[dr]
                        # 조건: 범위 내, 첫 방문, 1인 경우
                        if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc] and arr[nr][nc]:
                            # 방문처리, 다음 탐색 좌표로 추가
                            visit[nr][nc] = True
                            stack.append((nr, nc))
                ans += cnt
    result.append(ans)
for re in result:
    print(re)
