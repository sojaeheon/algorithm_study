# 길이가 N인 컨베이어 벨트가 있고,
# 길이가 2N인 벨트가 이 컨베이어 벨트를 위아래로 감싸며 돌고 있다
# 1~2N 번호
# 회전하면 1씩 움직인다
# i번 칸의 내구도는 Ai이다 
# 1번칸의 위치는 올리는 위치, N번칸의 위치를 내리는 위치
# 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소한다

# 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
# 그렇지 않다면 1번으로 돌아간다.

from collections import deque

# 2<= N <= 100, 1<= K <=2N
# 길이 N, 종료 K
n,k = map(int,input().split())
# 1<= A <= 1000
# 벨트의 내구도
a = deque(map(int,input().strip().split()))
robot = deque([False]*n)

result = 0

while True:
    # 로봇 넣어
    result += 1

    # 로봇이랑 컨베이어 벨트 돌려
    a.appendleft(a.pop())
    robot.appendleft(robot.pop())

    # 로봇 내려
    robot[-1] = False

    # 로봇 이동
    for i in range(n-2,-1,-1):
        if robot[i] and not robot[i+1] and a[i+1]>0:
            robot[i], robot[i+1] = False,True
            a[i+1] -= 1
            
    # (기존 코드에 있던 라인)
    robot[-1] = False

    # 로봇 올리기
    if a[0] > 0:
        robot[0] = True
        a[0] -= 1

    if a.count(0)>=k:
        print(result)
        break

