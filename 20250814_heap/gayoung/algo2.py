import sys, heapq

input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    num = int(input())
    if num != 0:
        heapq.heappush(lst, (abs(num), num))
    else:
        if lst:
            small = heapq.heappop(lst)
            print(small[1])
        else:
            print(0)
