'''
길이가 N인 컨베이어벨트 
길이가 2N인 벨트가 이 컨베이어 벨트를 위아래로 감싸며 도는 중

선입선출 
큐?덱?


'''

from collections import deque

N, K = map(int,input().split())
belt = deque(map(int,input().split()))
robot = deque([False]*N)

cnt = 0

while (1):
    cnt += 1

    belt.rotate(1)
    robot.rotate(1)

    robot[-1] = False

    # 뒤에서부터 체크해서 로봇 이동 
    # 현재 로봇이 있고, 다음 단계에 로봇이 없고, belt 내구도가 0보다 클 때만 
    for i in range(N-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1] > 0:
            robot[i], robot[i+1] = False, True
            belt[i+1] -= 1  # 내구도 -1

    # 마지막 로봇 없애기 
    robot[-1] = False

    # 로봇 올리기
    if belt[0] > 0:
        robot[0] = True
        belt[0] -= 1

    # 0 카운트 
    if belt.count(0) >= K:
        print(cnt)
        break