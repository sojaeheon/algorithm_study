'''
로봇청소기

NxM 크기의 직사각형 방
동서남북 방향으로 청소기가 바라봄

1. 현재 칸 청소 x -> 청소
2. 현재칸 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    1. 바라보는 방향을 유지한 채로 후진 가능시 후진
    2. 후진 불가능하면 멈추기

3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    1. 반 시계 방향으로 90도 회전
    2. 바라보는 방향 기준 앞쪽 칸이 청소되지 않은 빈칸인 경우 한 칸 전진
    3. 1번으로 돌아감

bfs
'''

def bfs(r,c,dir):
    global cnt # 개수 세기


    while True:
        # 청소할 곳 있는지 체크
        check = False
        # 1번 조건: 청소해야하면
        if matrix[r][c] == 0:
            matrix[r][c] =2
            cnt += 1

        # 4방향 확인
        for i in range(4):
            # 반시계 90도
            dir = (dir+3)%4 #90도 회전
            # 회전한 곳 확인
            nx, ny = r + pos[dir][0], c + pos[dir][1]
            if 0<= nx < N and 0<= ny < M and matrix[nx][ny] == 0:
                # 갈 수 있으면 이동
                r,c = nx,ny
                check = True
                break

        if not check:
            # 후진 하는 방향 -> 현재 방향 반대편
            back_dir = (dir+2)%4
            nx,ny = r+pos[back_dir][0], c + pos[back_dir][1]
            # 벽이 아닐 때 후진 가능
            if 0<= nx< N and 0 <= ny < M and matrix[nx][ny] != 1:
                r,c = nx, ny
            else:
                return
        
        

N , M = map(int,input().split())

cnt = 0 

pos = [(-1,0), (0,1), (1,0), (0,-1)]

r,c, d = map(int,input().split())
# d 방향 북 : 0, 동 : 1, 남 : 2, 서 : 3

# 0 : 청소되지 않은 빈 칸 / 1: 벽
matrix = [list(map(int,input().split())) for _ in range(N)]


bfs(r,c,d)

print(cnt)