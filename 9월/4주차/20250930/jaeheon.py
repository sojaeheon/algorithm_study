# N+1일째 퇴사를 하기 위해, 남은 N일 동안 최대한 많은 상담을 하려고 한다
# 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다
# 각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어짐

# dfs 풀이
# def dfs(day,money):
#     global max_result

#     # 퇴사일에 도달한 경우
#     if day == n:
#         max_result = max(max_result, money)
#         return

#     if day > n:
#         return

#     # 1) 오늘 상담을 하는 경우
#     if day + ti[day] <= n:
#         dfs(day + ti[day], money + pi[day])

#     # 2) 오늘 상담을 안 하고 넘어가는 경우
#     dfs(day + 1, money)

# n = int(input())

# ti =[]
# pi = []

# max_result = 0

# for _ in range(n):
#     t, p = map(int,input().split())
#     ti.append(t)
#     pi.append(p)

# dfs(0,0)

# print(max_result)


# dp 풀이
n = int(input())

ti =[]
pi = []

# dp 저장
dp = [0]*n

max_result = 0

for _ in range(n):
    t, p = map(int,input().split())
    ti.append(t)
    pi.append(p)

for i in range(n):
    
    # 다음값 = max(현재 저장된 값 + 현재값, 다음값)
