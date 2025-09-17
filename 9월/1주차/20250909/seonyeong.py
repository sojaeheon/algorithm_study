'''
# 에라토스테네스의 체
# 소수를 판별하는 알고리즘

어떤 수의 소수 여부를 확인할 때는 특정한 숫자의 제곱근까지만 약수의 여부를 검증하면
절반도 아니고 '제곱근'까지만 확인하면 되니까 범위가 확! 줄어든다!
'''
import math

def solve(num):
    for i in range(2, int(math.sqrt(num))+1):
        #sqrt: 제곱근을 구함 == num**0.5 (굳이 math안써도 됨)
        if num%i == 0: #약수가 있으면 
            return 0
    return num

test_case = int(input())

for t in range(1, test_case+1):
    a, b = map(int, input().split())
    total = 0

    for num in range(a+1, b):
        total += solve(num)

    print(f'#{t} {total}')

# 재연 가영 코드 참고!