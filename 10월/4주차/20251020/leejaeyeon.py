from collections import deque

def move():
    time = 0
    snake = deque([(0,0)])
    dir = 0
    while True:
        time += 1
        dx , dy = snake[0][0] + pos[dir][0], snake[0][1] + pos[dir][1]


        if not (0 <= dx < N and 0 <= dy < N):  # 벽에 부딪힘
            return time 
        
        if (dx,dy) in snake:
            return time
        
        snake.appendleft((dx,dy))

        if matrix[dx][dy] == 1:
            matrix[dx][dy] = 0
        else:
            snake.pop()

        if time in snake_pos:
            if snake_pos[time] == 'D':
                dir = (dir +1) % 4
            else:
                dir = (dir + 3) % 4



pos = [(0,1),(1,0),(0,-1),(-1,0)]

N = int(input())

K = int(input())

matrix = [[0]*N for _ in range(N)]
matrix[0][0] = 2 # 뱀 머리

for i in range(K):
    x,y = map(int,input().split())
    matrix[x-1][y-1] = 1 # 사과

# 뱀 방향 변환 횟수
L = int(input())
snake_pos = {}
# L : 왼, D : 오른쪽 90도
for i in range(L):
    x,c = input().split()
    snake_pos[int(x)] = c

print(move())