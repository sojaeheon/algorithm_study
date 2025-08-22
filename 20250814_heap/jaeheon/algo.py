import heapq

# 지금까지 백준이가 말한 수 중에서 중간값을 말해야한다
# 짝수개라면 중간에 있는 두 수중에서 작은 수를 말해야한다

# 힙의 특징 : 루트 노드가 가장 작은 값이다

n = int(input())

lst = []
result = []
for i in range(1,n+1):
    num = int(input())
    heapq.heappush(lst,num)
    print(lst)
    

