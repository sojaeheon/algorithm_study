def dfs(cnt, start):
    if cnt == M:
        # 최종 값
        print(*ans)
        return
    prev = None

    # 중복 가능
    for i in range(start, N):
        # 첫 방문이면서, 이전 값과 다른 경우에만
        if not visited[i] and prev != lst[i]:
            # 답 추가: 현재 값을 포함해서 탐색
            visited[i] = True
            ans.append(lst[i])
            # 탐색하기 :
            dfs(cnt + 1, i+1)
            # 답 제거
            visited[i] = False
            ans.pop()
            # 이전 값을 할당
            prev = lst[i]

# 정수, 고르는 개수
N, M = map(int, input().split())
# 숫자 값
lst = list(map(int, input().split()))
ans = []
lst.sort()
visited = [False] * N
# 개수, 시작 정수
dfs(0,0)