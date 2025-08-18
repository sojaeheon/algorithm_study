# N: 팀 수, S: 손상된 팀 수 R: 하나 더 가져 온 팀 수
N, S, R = map(int, input().split())
list_broken = list(map(int, input().split()))
list_more = list(map(int, input().split()))

# 정답 리스트 생성하기
list_ans = [1] * (N + 1)

# 손상된 팀 표시
for num in list_broken:
    list_ans[num] = 0

# 더 가져온 팀 표시
for num in list_more:
    list_ans[num] += 1

# 돌면서 나눠주기
for i in range(1, N + 1):
    # 내가 여분이 있다면,
    if list_ans[i] > 1:
        # 내 앞번호가 비어있다면, 나눠주기
        if not list_ans[i - 1]:
            list_ans[i - 1] = 1
            list_ans[i] -= 1
        # (리스트 인덱스 체크하고), 내 뒷번호가 비어있다면, 나눠주기
        elif i != N and not list_ans[i + 1]:
            list_ans[i + 1] = 1
            list_ans[i] -= 1
# 비어 있는 개수 세기
result = list_ans[1:].count(0)
print(result)
