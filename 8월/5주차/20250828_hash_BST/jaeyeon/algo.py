# 문자열 지옥에 빠진 호석 20166번
from collections import defaultdict

def dfs(x, y,current):
    cnt_dict[current] += 1

    # 종료조건
    if len(current) == max_len:
        return

    for i in range(8):
        # 범위 넘어갈 때 이동
        nx,ny = (x + pos[i][0])%N , (y + pos[i][1])%M
        dfs(nx,ny,current+matrix[nx][ny])



N, M, K = map(int,input().split())

# 상하좌우 + 대각선
pos = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

matrix = [list(map(str,input().strip())) for _ in range(N)]

# 신이 좋아하는 문자열 
god_str = [input().strip() for _ in range(K)]
# 신의 문자열 중 가장 긴 길이 저장
max_len = max(len(s) for s in god_str)


# 문자열마다의 개수를 저장 (ex. 'aaa' = 3 )
# 처음은 0으로 초기화
cnt_dict = defaultdict(int)

# matrix 순회
for i in range(N):
    for j in range(M):
        dfs(i, j, matrix[i][j])

# 문자열마다 개수 프린트
for god in god_str:
    print(cnt_dict[god])