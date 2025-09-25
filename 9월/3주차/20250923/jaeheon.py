# 청소하는 영역의 개수를 구하는 프로그램

# N x M 크기의 직사각형의 방
# 벽 또는 빈칸
# 청소기가 바라보는 방향이 있으며, 방향은 동, 서, 남, 북 => 델타탐색

# 현재 칸이 아직 청소되지 않은 경우, 현재 칸 청소
# 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
  # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한칸 후진하고 1번으로 돌아간다
  # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다
# 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
  # 반시계 방향으로 90도 회전
  # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한칸 전진
  # 1번으로 돌아간다

# 북,동,남,서
dir ={
  0:(-1,0), # 북
  1:(0,1),  # 동
  2:(1,0),  # 남
  3:(0,-1)  # 서
}


def clean_room(robot_r,robot_c,robot_d,room):
  count = 0

  while True:
    # -1이면 청소하지 않았다면
    if room[robot_r][robot_c] == 0:
      room[robot_r][robot_c] = -1
      count+=1
    
    flag = False

    for _ in range(4):
      robot_d = (robot_d + 3) % 4
      d_r, d_c = dir[robot_d]

      n_r = robot_r + d_r
      n_c = robot_c + d_c
      if room[n_r][n_c] == 0:
        robot_r,robot_c = n_r,n_c
        flag = True
        break
    
    if flag: continue

    b_d = (robot_d + 2) % 4
    b_r,b_c = robot_r + dir[b_d][0], robot_c + dir[b_d][1]

    if room[b_r][b_c] != 1:
      robot_r = b_r
      robot_c = b_c
    else: break

  return count
  
# 3<= n,m <= 50
n,m = map(int,input().split())

# 로봇의 좌표와 바라보는 방향
# 0 = 북, 1 = 동, 2 = 남, 3 = 서
robot_r,robot_c, robot_d = map(int,input().split())

# 0은 청소되지 않은 빈 칸, 1은 벽, 
room = [list(map(int,input().split())) for _ in range(n)]

result = clean_room(robot_r,robot_c,robot_d,room)
print(result)