
# 8개의 톱니를 가지고 있는 톱니바퀴 4개
# 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, 
# B는 A가 회전한 방향과 반대방향으로 회전하게 된다

from collections import deque

def rotate(wheel_num,dirt):
    if dirt == 1:
        arr[wheel_num].appendleft(arr[wheel_num].pop())
    else:
        arr[wheel_num].append(arr[wheel_num].popleft())

arr = [deque(map(int,list(input()))) for _ in range(4)]
k = int(input())

for _ in range(k):
    # 돌릴 바퀴와 방향
    wheel_num, dirt = map(int,input().split())
    wheel_num-=1
    
    # 어떤 톱니바퀴를 어떤 방향으로 돌릴지 저장
    rotation_info = [(wheel_num, dirt)]

    # 왼쪽 톱니바퀴들 전파 확인 
    current_dirt = dirt
    for i in range(wheel_num, 0, -1):
        # 현재 톱니(i)의 9시 방향(인덱스 6)과 왼쪽 톱니(i-1)의 3시 방향(인덱스 2) 비교
        if arr[i][6] != arr[i-1][2]:
            current_dirt *= -1  # 방향 반대로 전환
            rotation_info.append((i-1, current_dirt))
        else:
            # 극이 같으면 더 이상 전파되지 않으므로 중단
            break

    # 오른쪽 톱니바퀴들 전파 확인 
    current_dirt = dirt
    for i in range(wheel_num, 3):
        # 현재 톱니(i)의 3시 방향(인덱스 2)과 오른쪽 톱니(i+1)의 9시 방향(인덱스 6) 비교
        if arr[i][2] != arr[i+1][6]:
            current_dirt *= -1  # 방향 반대로 전환
            rotation_info.append((i+1, current_dirt))
        else:
            # 극이 같으면 더 이상 전파되지 않으므로 중단
            break
    
     # 2. 위에서 결정된 정보에 따라 한꺼번에 회전 실행
    for num, d in rotation_info:
        rotate(num, d)
    
# 3. 최종 점수 계산
score = 0
if arr[0][0] == 1: score += 1
if arr[1][0] == 1: score += 2
if arr[2][0] == 1: score += 4
if arr[3][0] == 1: score += 8

print(score)

    
    

