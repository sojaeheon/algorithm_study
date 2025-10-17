from itertools import combinations

pos = [(0,1),(0,-1),(1,0),(-1,0)]

N,M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

chickens = []
homes = []

result = float('inf')

# 치킨집, 집 좌표 저장
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            homes.append((i,j))
        elif matrix[i][j] == 2:
            chickens.append((i,j))

# 치킨집 M개 조합별 선택
for chicken in combinations(chickens,M):
    dist = 0
    # 모든 집 순회
    for nx, ny in homes:
        min_dist = float('inf')
        # 치킨집 좌표와 거리 확인
        for tx,ty in chicken:
            distance = abs(nx-tx) + abs(ny - ty)
            min_dist = min(distance, min_dist)
        # 가까운 거리 갱신
        dist += min_dist
    result = min(result,dist)
print(result) 
