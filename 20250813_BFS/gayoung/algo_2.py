from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

queue = deque()

visit = [False]*(N+1)
cnt = 0
# 앞에서부터 탐색
for i in range(1, N+1):
    # 방문 안했다면, 시작 노드로 설정
    if not visit[i]:
        # 새로운 연결요소 추가
        cnt += 1
        # 시작값, 방문처리
        queue = deque([i])
        visit[i] = True
        while queue:
            node = queue.popleft()
            for num in lst[node]:
                if not visit[num]:
                    visit[num] = True
                    queue.append(num)
print(cnt)

