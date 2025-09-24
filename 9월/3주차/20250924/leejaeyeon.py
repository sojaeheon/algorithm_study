'''
1. 국경선 공유하는 두 나라의 인구차 L명 이상, R명 이하 -> 하루 동안 국경선 엶
2. 위의 조건에 의해 열어야 하는 국경선이 모두 열리면 -> 이동 시작
3. 국경선이 열려있어 인접한 칸만을 이용해 이동이 가능하면 연합이라고 생각?
4. 연합을 이루고 있는 각 칸의 인구수는 (연합 인구수)/(연합이루고있는 칸의 개수) 소수점 버림
5. 연합 해체 후 국경선 닫기

인구이동이 며칠동안 발생하는지

while True
모든 곳 다 돌기 이중 for문
    bfs
    차이가 조건 내에 있으면
    방문처리 
    다 돌면 set저장된 좌표의 값들 모두 더하기 / len(visited)
    visited 좌표에 저장
cnt +1

check로 국경선 여는 곳이 있는지 체크
'''
from collections import deque

def bfs(row, col):
    visited[row][col] = True
    q = deque()
    q.append((row,col))
    total = matrix[row][col]

    union = set()
    union.add((row,col))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x + pos[i][0] , y+pos[i][1]

            if 0<= nx < N and 0<= ny <N and not visited[nx][ny]:
                if L <= abs(matrix[nx][ny] - matrix[x][y]) <= R:
                    visited[nx][ny] =True
                    union.add((nx,ny))
                    q.append((nx,ny))
                    total += matrix[nx][ny]

    return union, total
    


N, L, R = map(int, input().split())
pos = [(0,1),(0,-1),(1,0),(-1,0)]

matrix = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
while True:
    visited = [[False]*N for _ in range(N)]
    check = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union, total = bfs(i,j)
                if len(union) > 1:
                    check = True
                    num = total // len(union)
                    for x,y in union:
                        matrix[x][y] = num
    if not check:
        break
    cnt += 1

print(cnt)