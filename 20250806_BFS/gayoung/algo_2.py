from collections import deque


def solve():
    # 시작 숫자, 횟수
    queue = deque([(A, 0)])

    # queue 값이 없을 때까지 반복
    while queue:
        now = queue.popleft()
        # 시작 값, 횟수
        num, cnt = now[0], now[1]
        # print(num, cnt)
        # 값이 같으면, 종료
        if num == K:
            break

        else:
            # 다음 값 구하기
            num1 = num + 1
            num2 = num * 2
            # 방문 안했다면? & K 보다 값이 같거나 작다면,
            if num1 <= K and not visit[num1]:
                # 방문처리
                visit[num1] = True
                queue.append((num1, cnt + 1))
            if num2 <= K and not visit[num2]:
                # 방문처리
                visit[num2] = True
                queue.append((num2, cnt + 1))

    return print(cnt)


A, K = map(int, input().split())
# 방문: 이미 만든 값이면 또 만들 필요 없고, 만들어져 있다는 건, 지금 횟수보다 적다는 것
visit = [False] * 10000001

solve()

# print(ans)
