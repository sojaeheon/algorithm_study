'''
bfs
- 3가지의 경우의 수를 탐색해야 한다.
1. x+1
2. x-1
3. x * 2
시간을 구해야 한다  = cnt 같이 가야한다.

'''

'''
from collections import deque

N, K = map(int, input().split())
queue = deque()
# 시작 값 넣기 : start, cnt
queue.append((N, 0))
visit = [False] * 100001
while queue:
    num, cnt = queue.popleft()
    if num == K:
        break
    # 탐색하기
    # 1. 앞으로 가기
    queue.append((num + 1, cnt + 1))
    # 2. 뒤로 가기
    queue.append((num - 1, cnt + 1))
    # 3. 두배 앞으로 가기
    queue.append((num * 2, cnt + 1))
print(cnt)
'''

from collections import deque

N, K = map(int, input().split())
queue = deque()
# 시작 값 넣기 : start, cnt
queue.append((N, 0))
visit = [False] * 100001

while queue:
    num, cnt = queue.popleft()
    # K도달
    if num == K:
        break
    # 방문한 적 없음
    if not visit[num]:
        # 방문처리
        visit[num] = True
        for next in (num - 1, num + 1, num * 2):
            # 범위 내이면서, 첫 방문
            if 0 <= next <= 100000 and not visit[next]:
                queue.append((next, cnt + 1))

print(cnt)
