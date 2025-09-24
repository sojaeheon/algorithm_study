# N x N 크기의 땅
# 각각의 땅에는 나라가 하나씩 존재, 인접한 나라 사이에는 국경선이 있다

# 다음과 같은 인구이동 하루동안 진행(반복)
# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면,
# 두 나라가 공유하는 국경선을 오늘 하루 동안 연다
# 위 조건에 의 열어야하는 국경선이 모두 열렸따면, 인구 이동 시작
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다
# 연합을 이루고 있는 각 칸의 (인구수는 연합의 인구수/연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다
# 연합을 해체하고, 모든 국경선을 닫는다

from collections import deque

d_row = [-1,1,0,0]
d_col = [0,0,-1,1]

def population_move(row,col,visited,country,l,r):
  que = deque([(row,col)])
  visited[row][col]=True
  set_country = set()
  set_country.add((row,col))

  while que:
    c_row, c_col = que.popleft()

    for i in range(4):
      n_row, n_col = c_row + d_row[i], c_col + d_col[i]

      # 범위 밖으로 나간다면
      if not(0<=n_row<n and 0<=n_col<n):continue
      # 방문한 적 있으면
      if visited[n_row][n_col]: continue
      # l이상 r이하가 아니라면
      if not(l<=abs(country[c_row][c_col]-country[n_row][n_col])<=r):continue

      if (n_row,n_col) in set_country: continue

      visited[n_row][n_col] = True
      que.append((n_row,n_col))
      set_country.add((n_row,n_col))
  
  if len(set_country)>1:
    total = 0
    for x, y in set_country:
      total += country[x][y]
    new_val = total //len(set_country)
    for x, y in set_country:
      country[x][y] = new_val
    return True
  else:
    return False



# 1<=N<=50, 1<=L<=R<=100
n,l,r = map(int,input().split())
country = [list(map(int,input().split())) for _ in range(n)]

day = 0

while True:
  visited = [[False]*n for _ in range(n)]
  flag=False
  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        # 인구이동
        if population_move(i,j,visited,country,l,r): flag = True

  # 인구이동이 있었다면 day +=1
  if flag:
    day += 1
    # 인구이동이 없으면 break
  else:
    break

print(day)
