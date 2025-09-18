'''
덱으로 회전 + 상태 확인
'''


from collections import deque


# 바퀴 리스트 (줄마다 덱으로 입력)
wheel_list = [deque(map(int,input().strip())) for _ in range(4)]

# 회전횟수
K = int(input())

for i in range(K):
    # 톱니바퀴 번호, 방향
    n, dir = map(int,input().split())
    # print(wheel_list)
    # 방향 리스트
    n_dir = [0]*4
    # 처음 바퀴에 대한 방향 설정
    n_dir[n-1] = dir
    
    # 왼쪽
    left_dir = dir
    for i in range(n-1, 0 , -1):
        if wheel_list[i][-2] != wheel_list[i-1][2]:
            n_dir[i-1] = -n_dir[i]
        else:
            break

    right_dir = dir
    for i in range(n-1, 3):
        if wheel_list[i][2] != wheel_list[i+1][-2]:
            n_dir[i+1] = -n_dir[i]
        else:
            break

    for i in range(4):
        wheel_list[i].rotate(n_dir[i])
    # print(n_dir)

result = 0
if wheel_list[0][0]: result += 1
if wheel_list[1][0]: result += 2
if wheel_list[2][0]: result += 4
if wheel_list[3][0]: result += 8

print(result)