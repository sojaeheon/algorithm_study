# 재귀 크기 늘리기
import sys
sys.setrecursionlimit(100000)

# dfs 함수 (x좌표, y좌표, 방문여부, 적록색약 여부)
def dfs(x,y, visit, check):
    visit[x][y] = 1   # 방문
    for i in range(4):   # 상하좌우 순회
        dx, dy = x + pos[i][0], y + pos[i][1]   # pos의 좌표대로 움직이기
        # 만약 좌표 내에서 움직이고 아직 방문하지 않은 곳일 때,
        if (0 <= dx < N) and (0 <= dy < N) and (visit[dx][dy] == 0): 
            if (rgb[x][y] == rgb[dx][dy]):   # 동일한 색상이면
                dfs(dx,dy, visit, check)
            # 만약 적록색약이라면
            elif check and ((rgb[x][y] == 'R'and rgb[dx][dy] == 'G') or (rgb[x][y] == 'G' and rgb[dx][dy] == 'R')):
                dfs(dx,dy, visit, check)

    return 

# 입력 받기
N = int(input())
rgb = [list(input().strip()) for _ in range(N)]

# 적록색약인 사람과 아닌 사람의 방문 리스트 따로 작성
visited = [ ([0] * N) for _ in range(N)]
rgb_visited = [ ([0] * N) for _ in range(N)]

# 적록색약인지 체크하는 변수
check = False
pos = [(-1,0),(1,0),(0,-1),(0,1)]


# 구역 결과값 변수
cnt = 0
cnt_rgb = 0


# 그리드 크기만큼 순회
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:          # 적록색약 X
            dfs(i,j,visited,check=False)
            cnt += 1                    # 한 구역을 다 돌았다면 +1

        # 적록색약
        if rgb_visited[i][j]== 0:          # 적록색약 O
            dfs(i,j,rgb_visited,check=True)
            cnt_rgb += 1                    # 한 구역을 다 돌았다면 +1

print(cnt,cnt_rgb)