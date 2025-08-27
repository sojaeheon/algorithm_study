'''
- 루트 출발
- 왼쪽 -> 부모 -> 오른
- 중위순회
'''

''' 
def dfs(depth, list):
    # 종료조건
    if depth == K:
        return

    # 루트 찾기
    root = len(list) // 2

    # root 기록하기
    result[depth].append(list[root])

    # 다음 탐색하기
    left = list[:root]
    right = list[root+1:]
    dfs(depth+1, left)
    dfs(depth+1, right)


# 깊이 K
K = int(input())
# 방문한 빌딩의 번호 순서대로
lst = list(map(int, input().split()))

# 결과 담기
result = [[] for _ in range(K)]

# dfs 호출
dfs(0, lst)
for num in result:
    print(*num)

'''
'''
def dfs(depth, start, end):
    if depth == K:
        return

    # 중간 값 찾기
    mid = (start+end) // 2
    result[depth].append(lst[mid])

    # 다음 값 찾기
    # 왼쪽 탐색
    dfs(depth+1, start, mid-1)
    # 오른쪽 탐색
    dfs(depth+1, mid+1, end)


K = int(input())
# 방문한 빌딩의 번호 순서대로
lst = list(map(int, input().split()))
result = [[] for _ in range(K)]

# depth, start, end
dfs(0, 0, len(lst) - 1)
for num in result:
    print(*num)
'''
from collections import deque

K = int(input())
# 방문한 빌딩의 번호 순서대로
lst = list(map(int, input().split()))
result = [[] for _ in range(K)]
queue = deque()
# 시작 넣기 : depth, start, end
queue.append((0, 0, len(lst) - 1))

while queue:
    depth, start, end = queue.popleft()
    # 루트노드 찾기
    mid = (start + end) // 2

    # 정답에 넣기
    result[depth].append(lst[mid])

    if depth+1 < K:
        # 왼쪽 탐색
        queue.append((depth + 1, start, mid - 1))

        # 오른쪽 탐색
        queue.append((depth + 1, mid + 1, end))

for num in result:
    print(*num)
