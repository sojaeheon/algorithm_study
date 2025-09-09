# 에라토스테네스의 체
import math

def sol(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return 0
    return num

T = int(input())

for test_case in range(1,T+1):
    a,b = map(int, input().split())

    result = 0

    for num in range(a+1, b):
        result += sol(num)

    print(f"#{test_case} {result}")