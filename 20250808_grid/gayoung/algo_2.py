# N: 종류 수 K: 금액
N, K = map(int, input().split())

lst = [int(input()) for _ in range(N)]
# 큰 값 순으로 정렬 : 동저의 최솟값을 구해야 하므로!
lst.sort(reverse=True)

# 계산하기
cnt = 0
target = K
for coin in lst:
    if coin > target:
        continue
    else:
        # 개수 구하고, 남은 값 계산
        cnt += target // coin
        target = target % coin
print(cnt)
