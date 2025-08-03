# 입력
n = int(input())  # 탑의 개수
top_list = list(map(int,input().split())) # 탑들의 높이

result = [] # 결과
stack = [] # 스택(인덱스,높이)

# 왼쪽부터 순회
for idx in range(n):
    # 스택에 값이 존재하고 해당 값의 마지막 탑의 높이가 현재 탑보다 작거나 같을 경우
    # 스택에서 제거 -> 레이저 안닿기 때문
    while stack and stack[-1][1] <= top_list[idx]:
        stack.pop()
    # 스택에 남아있다면 마지막에 있는 탑이 레이저를 수신한다는 것이므로 인덱스 추가
    if stack:
        result.append(stack[-1][0])
    # 없으면 레이저 수신한 탑이 없다는 의미이므로 0 추가
    else:
        result.append(0)

    # 현재 탑을 스택에 추가 (다음 탑의 레이저 수신여부 확인 위해)
    stack.append((idx+1,top_list[idx]))

print(*result)