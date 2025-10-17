# 구사과는 각 칸(r,c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발

# 공기청정기는 항상 1번 열에 설치되어 있고 , 크기는 "두 행을 차지한다"

# 1초 동안 발생하는 작업
# 1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 칸에서 동시에 일어난다
# - (r,c)에 있는 미세먼지는 인접한 네 방향으로 확산
# - 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다
# - 확산되는 양은 A/5이고, 소수점은 버린다.
# - (r,c)에 남은 미세먼지의 양은 a - (a/5) * (확산된 방향의 개수)

# 2. 공기 청정기가 작동한다
# - 공기청정기에서는 바람이 나온다
# - 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다
# - 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다
# - 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다

d_row = [-1,1,0,0]
d_col = [0,0,-1,1]

# 공기청정
def fine_dust_expand(room):
    temp = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if room[r][c] > 0:
                spread = room[r][c] // 5
                count = 0
                for d in range(4):
                    nr, nc = r + d_row[d], c + d_col[d]
                    if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                        temp[nr][nc] += spread
                        count += 1
                room[r][c] -= spread * count
    # 확산 결과 반영
    for r in range(R):
        for c in range(C):
            room[r][c] += temp[r][c]
    

# 미세먼지 확산
def clean_room(room, machine_idx):
    up,down = machine_idx[0][0],machine_idx[1][0]

    # 아래 → 위
    for r in range(up-1, 0, -1):
        room[r][0] = room[r-1][0]
    # 왼 → 오
    for c in range(C-1):
        room[0][c] = room[0][c+1]
    # 위 → 아래
    for r in range(up):
        room[r][C-1] = room[r+1][C-1]
    # 오 → 왼
    for c in range(C-1, 1, -1):
        room[up][c] = room[up][c-1]
    room[up][1] = 0  # 공기청정기 옆칸 정화

    # 🔹 아래쪽(시계)
    for r in range(down+1, R-1):
        room[r][0] = room[r+1][0]
    for c in range(C-1):
        room[R-1][c] = room[R-1][c+1]
    for r in range(R-1, down, -1):
        room[r][C-1] = room[r-1][C-1]
    for c in range(C-1, 1, -1):
        room[down][c] = room[down][c-1]
    room[down][1] = 0

R,C,T = map(int,input().split())

room = [list(map(int,input().split())) for _ in range(R)]

fine_dust_idx = []
machine_idx =[]

# 먼지 위치 저장
for r in range(R):
    for c in range(C):
        if room[r][c] != 0:
            if room[r][c] == -1:
                machine_idx.append((r,c))

# 초 세기
for _ in range(T):
    # 1번 미션 수행(공기확산)
    fine_dust_expand(room)
    # 2번 미션 수행(먼지청소)
    clean_room(room, machine_idx)

# 다 끝났을때 모든 방을 돌면서 먼지들의 합 구하기
result = 0
for r in range(R):
    for c in range(C):
        if room[r][c] not in (-1,0):
            result += room[r][c]

print(result)
