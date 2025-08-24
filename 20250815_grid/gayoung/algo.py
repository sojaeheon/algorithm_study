import sys
input = sys.stdin.readline

N = int(input())

list_a = list(map(int,input().split()))
list_b = list(map(int,input().split()))

# visit 써서 문제 풀기?
# list_b는 바꾸지 않음 , a의 수만

# 가장 큰 값과 가장 작은 값
list_b.sort(reverse=True)
list_a.sort()

# 계산하기
ans = 0
for i in range(N):
    ans += list_a[i] * list_b[i]
print(ans)