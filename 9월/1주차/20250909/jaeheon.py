def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime

# 입력 처리
T = int(input())

MAX = 1000000

is_prime = sieve(MAX)

for tc in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        a, b = b, a   # 범위 정리
    total = sum(i for i in range(a+1, b) if is_prime[i])
    print(f"#{tc} {total}")