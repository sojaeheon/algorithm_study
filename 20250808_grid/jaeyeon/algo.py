import math 

# 웅덩이 개수, 널빤지 크기 입력
n, L = map(int,input().split())

# 웅덩이 시작, 끝 정보 리스트
pool_list = []

# 웅덩이 개수만큼 시작, 끝 리스트 받아서 pool_list에 추가
for i in range(n):
    s, e = map(int,input().split())
    pool_list.append([s,e])


cnt = 0 # 널빤지 개수 입력
plank_end = 0   # 널빤지 끝점 체크 
pool_list.sort(key= lambda x:(x[1]))    # 웅덩이 끝점을 기준으로 정렬


# 웅덩이 개수만큼 순회
for s,e in pool_list:
    # print(s,e)
    if plank_end < s:       # 만약 널빤지 끝점이 웅덩이 시작점보다 이전에 있다면
        plank_end = s       # 널빤지 끝점을 웅덩이 시작 지점으로 이동
    # 웅덩이 크기 / 널빤지 크기 -> 올림 함수 사용함으로써 웅덩이 전체 덮기
    # ex) 웅덩이크기 : 5, 널빤지 크기 : 3 -> 5/3 = 1 웅덩이를 다 못덮음
    # ceil(5/3) -> 올림하여 2가 나옴으로써 웅덩이 전체를 덮을 수 있음   
    cnt += math.ceil((e-plank_end) / L)
    plank_end += math.ceil((e-plank_end) / L) * L
    # print(plank_end)

# 출력
print(cnt)