'''
상어 초등학교

학생 번호 + 좋아하는 학생 4명

1. 한 명씩 순서대로 배치
2. 인접한 4칸 중 좋아하는 학생이 가장 많이 있는 칸
3. 1번 조건이 여러 개면 인접한 빈 칸이 가장 많은 칸
4. 여러 개 -> 행 번호 작은 칸 -> 열 번호 작은 칸
'''

n = int(input())

data = [[0]*n for _ in range(n)]

students = [list(map(int,input().split())) for _ in range(n*n)]

pos  = [(-1,0),(1,0),(0,-1),(0,1)]

# 학생 : 좋아하는 학생들
like = {s[0] : s[1:] for s in students}

for student, *friends in students:
    avail = []

    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                prefer, empty = 0,0
                for k in range(4):
                    nx, ny = i + pos[k][0], j + pos[k][1]
                    if 0 <= nx <n and 0 <= ny < n:
                        if data[nx][ny] in friends:
                            prefer += 1

                        if data[nx][ny] == 0:
                            empty += 1
                # 음수로 저장해서 최대값이 우선되도록
                avail.append((-prefer, -empty, i,j))

    # 조건대로 정렬 (좋아하는 학생 수 > 빈칸 수 > 행 > 열)
    avail.sort()

    p,e,x,y = avail[0]
    data[x][y] = student

score = 0
for i in range(n):
    for j in range(n):
        student = data[i][j]
        cnt = 0
        for k in range(4):
            nx, ny = i + pos[k][0], j + pos[k][1]
            if 0 <= nx <n and 0 <= ny < n:
                if data[nx][ny] in like[student]:
                    cnt += 1
        if cnt > 0:
            score += 10**(cnt -1)

print(score)