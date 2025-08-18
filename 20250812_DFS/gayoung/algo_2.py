def dfs(node):
    # global 선언
    global num

    # 재귀 함수 호출
    visited[node] = True
    for re in result[node]:
        if not visited[re]:
            visited[re] = True
            num += 1
            dfs(re)


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
