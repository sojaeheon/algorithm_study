from collections import deque

# 방향 0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위
d_row = [0, 1, 0, -1]
d_col = [1, 0, -1, 0]

def game_start(apple_map, commands):
    N = len(apple_map)
    que = deque(commands)
    direction = 0  # 처음 방향은 오른쪽
    snake = deque([(0, 0)])  # 뱀의 위치
    time = 0  # 시간 카운트
    next_turn_time, next_turn_dir = que.popleft() if que else (None, None)

    while True:
        time += 1
        head_r, head_c = snake[0]
        n_r, n_c = head_r + d_row[direction], head_c + d_col[direction]

        # 1️⃣ 벽에 부딪히면 종료
        if not (0 <= n_r < N and 0 <= n_c < N):
            return time

        # 2️⃣ 자기 몸에 부딪히면 종료
        if (n_r, n_c) in snake:
            return time

        # 3️⃣ 머리 이동
        snake.appendleft((n_r, n_c))

        # 4️⃣ 사과 확인
        if apple_map[n_r][n_c] == 1:
            apple_map[n_r][n_c] = 0  # 사과 먹고 꼬리 유지
        else:
            snake.pop()  # 사과 없으면 꼬리 제거

        # 5️⃣ 방향 전환 시간 도달 시 회전
        if next_turn_time is not None and time == next_turn_time:
            if next_turn_dir == 'L':
                direction = (direction - 1) % 4
            elif next_turn_dir == 'D':
                direction = (direction + 1) % 4
            if que:
                next_turn_time, next_turn_dir = que.popleft()
            else:
                next_turn_time, next_turn_dir = (None, None)


# ------------------- 입력 -------------------
N = int(input())
K = int(input())

apple_map = [[0] * N for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    apple_map[r - 1][c - 1] = 1

L = int(input())
commands = []
for _ in range(L):
    x, c = input().split()
    commands.append((int(x), c))

print(game_start(apple_map, commands))
