from collections import deque

# 8 방향
d_row = [0,-1,-1,-1,0,1,1,1]
d_col = [-1,-1,0,1,1,1,0,-1]

# 대각선 탐색
diagonal = [(-1,-1),(-1,1),(1,1),(1,-1)]


# 구름 이동 후 물 증가
# 현재 맵 상태와, 구름 위치, 이동 방향, 이동 거리를 입력받는다
def cloud_move(arr, cloud_idx, d, s):
    
    # 이동 후 위치를 저장해 줄 리스트 변수
    re_cloud = []    

    # 해당 방향으로 이동
    while cloud_idx:
        n_row, n_col = cloud_idx.popleft()
        # 이동
        n_row = (n_row + d_row[d] * s) % N
        n_col = (n_col + d_col[d] * s) % N

        arr[n_row][n_col] += 1  # 비 내리기
        re_cloud.append((n_row, n_col))


    # 구름이 위치한 칸에 물 채우기
    for r,c in re_cloud:
        count = 0
        # 현재위치에서 대각선 탐색
        for dr,dc in diagonal:
            n_row,n_col = r+dr,c+dc
            if not(0<=n_row<N and 0<=n_col<N): continue
            if arr[n_row][n_col]: count += 1

        # 구름이 있던 칸 물채우기
        arr[r][c] +=  count

    return re_cloud

# 순회하면서 구름 생성
def cloud_create(arr,cloud_idx):
    new_cloud = []
    prev_clouds = set(cloud_idx)

    # 구름이 있었던 칸을 제외한 나머지 칸들 중 물의 양이 2이상인 칸에 구름 생성
    for r in range(N):
        for c in range(N):
            if arr[r][c]>=2 and ((r,c) not in prev_clouds):
                # 구름이 생기면 물의 양이 2만큼 줄어든다
                new_cloud.append((r,c))
                arr[r][c] -= 2
    cloud_idx.clear()

    return new_cloud

# 데이터 입력받기
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 구름 위치
cloud_idx = deque([(N-1,0),(N-1,1),(N-2,0),(N-2,1)])

# 결과값 반환
result = 0

for i in range(M):
    
    d,s = map(int,input().split())

    # 구름 이동
    lst = cloud_move(arr,cloud_idx,d-1,s)
    cloud_idx.extend(lst)
    
    # 구름 생성
    if i != M:
        new_lst = cloud_create(arr,cloud_idx)
        cloud_idx.extend(new_lst)

for a in arr:
    result += sum(a)

print(result)
    
    


