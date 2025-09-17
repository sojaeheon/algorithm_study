# 방향 (동, 서, 북, 남)
dir = {
    1: (0, 1),
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0)
}

# 주사위 [위, 아래, 북, 남, 서, 동]
dice = [0, 0, 0, 0, 0, 0]

def dice_rotate(command):
    top, bottom, north, south, west, east = dice
    if command == 1:  # 동쪽
        dice[0], dice[1], dice[4], dice[5] = west, east, bottom, top
    elif command == 2:  # 서쪽
        dice[0], dice[1], dice[4], dice[5] = east, west, top, bottom
    elif command == 3:  # 북쪽
        dice[0], dice[1], dice[2], dice[3] = south, north, top, bottom
    elif command == 4:  # 남쪽
        dice[0], dice[1], dice[2], dice[3] = north, south, bottom, top

n, m, x, y, k = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

for command in commands:
    dx, dy = dir[command]
    nx, ny = x + dx, y + dy

    # 범위 벗어나면 무시
    if not (0 <= nx < n and 0 <= ny < m):
        continue

    # 주사위 회전
    dice_rotate(command)

    # 지도와 주사위 바닥값 교환
    if map_arr[nx][ny] == 0:
        map_arr[nx][ny] = dice[1]
    else:
        dice[1] = map_arr[nx][ny]
        map_arr[nx][ny] = 0

    # 윗면 출력
    print(dice[0])

    # 좌표 업데이트
    x, y = nx, ny
    