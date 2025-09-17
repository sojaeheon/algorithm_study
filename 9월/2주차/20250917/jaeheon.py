
N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 충분히 큰 초기값 (문제의 값 범위를 벗어나지 않도록 여유있게)
max_val = -10**100
min_val = 10**100

def dfs(idx, current, add, sub, mul, div):
    global max_val, min_val
    if idx == N:
        if current > max_val:
            max_val = current
        if current < min_val:
            min_val = current
        return

    nxt = numbers[idx]

    if add > 0:
        dfs(idx+1, current + nxt, add-1, sub, mul, div)
    if sub > 0:
        dfs(idx+1, current - nxt, add, sub-1, mul, div)
    if mul > 0:
        dfs(idx+1, current * nxt, add, sub, mul-1, div)
    if div > 0:
        # 나눗셈: 0 방향(절단)으로 정수 나눗셈
        # 분모가 0인 경우는 문제 입력에서 없다고 가정(있다면 예외처리 필요)
        if nxt == 0:
            return
        q = abs(current) // abs(nxt)
        # 부호가 다르면 음수
        # 두 수의 부호가 다르면 음수로 바꾸기
        if (current < 0 and nxt > 0) or (current > 0 and nxt < 0):
            q = -q
        dfs(idx+1, q, add, sub, mul, div-1)

# 시작은 numbers[0]에서 시작해서 idx=1 부터 다음 숫자 적용
dfs(1, numbers[0], add, sub, mul, div)

print(max_val)
print(min_val)
