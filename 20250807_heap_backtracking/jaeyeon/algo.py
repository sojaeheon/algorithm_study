import heapq

n = int(input())

meeting_list = []

for i in range(n):
    s, e = map(int,input().split())
    meeting_list.append((s,e))

meeting_list.sort()

room_list = []
heapq.heappush(room_list, meeting_list[0][1])


for i in range(1, n):
    s,e = meeting_list[i][0], meeting_list[i][1]

    if s >= room_list[0]:
        heapq.heappop(room_list)
        heapq.heappush(room_list, e)
    else:
        heapq.heappush(room_list, e)

print(len(room_list))