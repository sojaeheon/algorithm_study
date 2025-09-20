'''
주사위 굴리기
NxM 지도
(r,c)
r은 북쪽으로부터 떨어진 칸의 개수
c는 서쪽으로부터 떨어진 칸의 개수

지도가 0 이면 주사위의 바닥면의 값이 복사
지도가 0이 아니면 주사위 바닥면에 칸에 쓰인 수 복사 & 칸에 쓰인 수는 0

주사위 상단에 쓰인 값 구하기
'''

def sol(position):
    if position == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4],dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4],dice[2]
    elif position == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4],dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4],dice[3]
    elif position == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4],dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5],dice[1]
    elif position == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4],dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0],dice[4]



# 지도 크기 NxM, 주사위 좌표 x,y 명령 개수 K
N, M, x,y, K = map(int,input().split())
# 위,북, 동, 서, 남, 아래
dice = [0,0,0,0,0,0]

pos = {
    1 : (0,1),
    2 : (0,-1),
    3 : (-1,0),
    4 : (1,0)
}

map_list = [list(map(int,input().split())) for _ in range(N)]

# 동 1 서 2 북 3 남 4
pos_list = list(map(int,input().split()))

for position in pos_list:
    dx,dy = pos[position]
    nx, ny = x + dx, y + dy

    if (nx < 0 or nx >= N) or (ny < 0 or ny >= M):
        continue

    sol(position)

    if map_list[nx][ny] == 0:
        map_list[nx][ny] = dice[5]
    else:
        dice[5] = map_list[nx][ny]
        map_list[nx][ny] = 0
    print(dice[0])

    x,y = nx, ny