N = int(input())

"최소 개수 => 5킬로 봉투를 최대한 사용, 3킬로만 사용할 수 있으므로 !"
# 5킬로에서 하나씩 줄여가면서 : N //5 ~ 0 까지 루프 돌리기
for cnt_5 in range (N//5, -1, -1 ):
    cnt_3 = (N - (cnt_5 * 5)) // 3  # 5킬로 봉투량 뺀 무게를 3킬로로 나눠서 봉지 수 구하기
    if (cnt_5 * 5) +  (cnt_3 * 3) == N:
        print(cnt_5 + cnt_3)
        break
else:
    print(-1)