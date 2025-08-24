import heapq
import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    num = int(input())
    # num 정수면
    if num != 0:
		    # 힙에 추가
        heapq.heappush(lst, -num)
    # 0이면,
    else:
		    # lst 비어있지 않으면,
        if lst:
            large = -heapq.heappop(lst)
            print(large)
        # 비어 있으면 0 출력
        else:
            print(0)
