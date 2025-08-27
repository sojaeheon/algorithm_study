def dfs(node):
    # global 선언
    global num

    # 재귀 함수 호출
    visited[node] = True    # 방문한 노드를 방문 기록하기
    for re in result[node]: # 해당 노드와 연결된 다른 노드 탐색하기
        if not visited[re]: # 만약, 처음 방문한 노드라면,
            visited[re] = True  # 방문 처리하고
            num += 1            # 감염시켰으므로 감염수 + 1
            dfs(re)             # 다음 노드 탐색하기


N = int(input())
pair = int(input())
# 값을 저장할 리스트 생성
result = [[] for _ in range(N + 1)]
for _ in range(pair):
    pair1, pair2 = map(int, input().strip().split())
    result[pair1].append(pair2)
    result[pair2].append(pair1)

visited = [False] * (N + 1)
num = 0
dfs(1)
print(num)