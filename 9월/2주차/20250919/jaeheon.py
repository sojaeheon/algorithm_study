
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
