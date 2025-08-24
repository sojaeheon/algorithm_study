import heapq
import sys


n = int(sys.stdin.readline())
left_heap = []
right_heap = []

for i in range(n):
    num = int(sys.stdin.readline())
    
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)     # 최대힙
    else:
        heapq.heappush(right_heap, num)     # 최소힙
    
    if right_heap and right_heap[0] < -left_heap[0]:
        right = heapq.heappop(right_heap)
        left = heapq.heappop(left_heap)

        heapq.heappush(left_heap, -right)
        heapq.heappush(right_heap, -left)
    print(-left_heap[0])