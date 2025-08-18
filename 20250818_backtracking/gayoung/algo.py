def dfs(nums, total, start):
    global cnt
    if nums >= 1 and total == S:
        cnt += 1

    for i in range(start, N):
        dfs(nums + 1, total + lst[i], i + 1)


# N과 S 점수
N, S = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
dfs(0, 0, 0)
print(cnt)