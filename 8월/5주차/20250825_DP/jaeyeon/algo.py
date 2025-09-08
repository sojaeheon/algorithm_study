N = int(input())

time = [0] * (N+1)
price = [0] * (N+1)
dp = [0] * (N+2)

# 시간, 금액 입력
for i in range(1,N+1):
    time[i], price[i] = map(int,input().split())


for i in range(1,N+1):
    # 이전 날 상담을 안했을 때, 값 저장하기 위함
    dp[i+1] = max(dp[i+1],dp[i])

    # 상담 끝나는 날 까지의 최대 이익 갱신
    if i + time[i] <= N+1:
        # dp에는 해당 날짜까지의 최대 금액이 들어있음
        dp[i+time[i]] = max(dp[i + time[i]],dp[i]+price[i])

print(max(dp))