<<<<<<< HEAD
# N x N크기의 공간, 물고기 M 마리, 아기상어 1마리
# 처음에 아기상어의 크기는 2, 
# 아기 상어는 1초에 상하좌우로 인접한 한 칸 씩 이동한다
# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다, 자신의 킉보다 작은 물고기만 먹을 수 있다.
# 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다
# 먹을 고기가 없으면 엄마 호출
# 먹을 수 있는 물고기가 1마리라면, 그 물고기 먹어
# 먹을 수 있는 물고기가 1마리보다 많다면, 가장 가까운 물고기를 먹어
# # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값
# # 거리가 가까운 물고기가 ㅁ낳다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼족 먹어
# 자신의 크기와 같은 수의 물고기를 먹으면 크기가 1 증가
# 엄마 호출하면 프로그램 종료
# N(2<= N <= 20)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

baby_size = 2
=======

d_row = [1,-1,0,0]
d_col = [0,0,1,-1]

def find_fish(row, col, arr,baby_size):
  visited = [[False]* N for _ in range(N)]

  eat = []
  que = [(row,col,0)]
  visited[row][col] = True

  min_time = 10**9

  while que:
    c_row,c_col, c_time =que.pop(0)

    if min_time < c_time: break
    
    for i in range(4):
      n_row = c_row + d_row[i]
      n_col = c_col + d_col[i]

      # 범위를 벗어나면
      if not(0<=n_row<N and 0<=n_col<N): continue
      if visited[n_row][n_col]: continue
      # 물고기가 더 크면
      if arr[n_row][n_col] >baby_size : continue

      visited[n_row][n_col] = True
      que.append((n_row, n_col, c_time+1))
            
      # 먹을 수 있는 물고기 발견
      if 0 < arr[n_row][n_col] < baby_size:
        eat.append((c_time+1, n_row, n_col))
        min_time = c_time+1  # 최소 거리 업데이트
  
  if not eat:
    return 0,0,0,False
  
  # 거리, 행, 열 순 정렬 
  eat.sort()
  dist, fr, fc = eat[0]
  return dist, fr, fc, True


N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

# 아기 상어 초기 사이즈
baby_size = 2
# 상어 위치
baby_row,baby_col = 0,0
# 먹은 개수
eat_count = 0
# 총 시간
time = 0

for i in range(N):
  for j in range(N):
    if arr[i][j] == 9:
      baby_row,baby_col = i,j
      arr[i][j] = 0

while True:   
  re_time,fish_r,fish_c,flag = find_fish(baby_row,baby_col,arr,baby_size)

  if not flag : break

  time += re_time
  baby_row, baby_col = fish_r, fish_c
  arr[fish_r][fish_c] = 0
  eat_count += 1
  

  if eat_count == baby_size:
    baby_size += 1
    eat_count = 0
  

print(time)
>>>>>>> d76f0586adb5eb7174a8c4f34fa4516685a71558
