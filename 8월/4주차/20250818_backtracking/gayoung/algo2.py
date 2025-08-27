import sys
input = sys.stdin.readline
def dfs(cnt, now):
    global max_value
    # N개를 다 순회했으면,
    if cnt == N:
        temp = 0
        # 리스트를 순회하면서 값을 계산, 갱신한다
        for i in range(N - 1):
            temp += abs(now[i] - now[i + 1])
        max_value = max(temp, max_value)
        return

    # lst 앞에서부터 순회 한다
    for i in range(N):
        # 방문하지 않았다면,
        if not visit[i]:
            # 방문처리 , 값넣기
            visit[i] = True
            now.append(lst[i])
            # 다음 수 탐색
            dfs(cnt + 1, now)
            # 재 탐색을 위해 방문 지우기, 값 지우기
            visit[i] = False
            now.pop()


N = int(input())
lst = list(map(int, input().split()))
visit = [False] * N
max_value = 0
dfs(0, [])
print(max_value)
