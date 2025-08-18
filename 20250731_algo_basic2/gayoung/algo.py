'''
# 가장 왼쪽 = lst[0]을 든다.
# 다른 계란의 [내구성]이 lst[0][무게]보다 작은데, 이 중에 가장 큰 값에 해당해야함 
# 다음 계란을 든다, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료한다.
즉, == 순회한다  
# 
'''


N = int(input())
lst = []
ans = 0
for _ in range(N):
   lst.append(list(map(int, input().split())))
   # [[8, 5], [1, 100], [3, 5]] / [내구성, 무게]

# 계란 1개면 깰 수 없으니까 0
for i in range(len(lst)):
    if N == 1 :
        ans = 0



 
    
