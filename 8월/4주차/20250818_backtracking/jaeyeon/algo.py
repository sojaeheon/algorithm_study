from itertools import combinations

pos = [(0,1),(0,-1),(1,0),(-1,0)]

# 입력
N,M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

chickens = [] # 치킨집 리스트 (2)
homes = [] # 집 리스트 (1)

result = float('inf')

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            homes.append((i,j))
        elif matrix[i][j] == 2:
            chickens.append((i,j))

for chicken in combinations(chickens, M):
    distance = 0
    for nx, ny in homes:
        min_dist = float('inf')
        for tx,ty in chicken:
            dist = abs(nx-tx) + abs(ny-ty)
            min_dist = min(min_dist,dist)
        distance += min_dist
    result = min(result, distance)

print(result)