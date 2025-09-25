# 교실은 NxN크기의 격자
# 학생수 N^2 1~N^2

# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다
# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은칸으로
# 그러한 칸도 여러개이면 열의 번호가 가장 작은 칸으로 자리를 정한다

d_r = [-1,1,0,0]
d_c = [0,0,-1,1]

def find_seat(student_num, seat):
  
  seat_lst = []

  # 모든 자리 탐색
  for r in range(N):
    for c in range(N):
      # 현재 자리가 정해져 있다면 다음
      if seat[r][c] != 0 : continue

      empty_count, friend_count = 0,0
      # 정해져있지 않다면 상하좌우 탐색
      for i in range(4):
        n_r = r + d_r[i]
        n_c = c + d_c[i]

        if not(0<=n_r<N and 0<=n_c<N): continue

        if seat[n_r][n_c] == 0: empty_count +=1
        if seat[n_r][n_c] in dic[student_num]: friend_count +=1
      seat_lst.append((-friend_count,-empty_count,r,c))
  
  seat_lst.sort()
  seat[seat_lst[0][2]][seat_lst[0][3]] = student_num



N = int(input())
commands = [list(map(int,input().split())) for _ in range(N**2)]
seat = [[0]*N for _ in range(N)]

dic ={}
result = 0
for command in commands:
  student_num = command[0]
  dic[student_num] = set(command[1:])

  find_seat(student_num, seat)

for r in range(N):
  for c in range(N):
    count = 0
    for i in range(4):
      n_r = r + d_r[i]
      n_c = c + d_c[i]

      if not(0<=n_r<N and 0<=n_c<N): continue
      if seat[n_r][n_c] in dic[seat[r][c]]: count+=1
    
    if count > 0:
      result += 10 ** (count - 1)
print(result)
      