'''
# SWEA 부분 집합의 합
1~N 까지 양의 정수를 원소로 갖는 집합
모든 부분 집합에 대해 원소의 합이 K인 경우의 수 M 알아내기

부분 집합 개수 : 2^N
모든 부분 집합 확인하는 것 보다 정수 i를 부분 집합에 포함시킬지 고려할 때 이미 부분집합에 포함시킨 원소의 합 S와
아직 고려하지 않은 숫자들의 합 R을 동시에 활용하기

'''

# 현재 숫자, 현재까지의 합
def sol(idx, current_sum):
    # 이미 다녀간 곳이면 패스
    if (idx, current_sum) in memo:
        return memo[(idx,current_sum)]
    
    # 가지치기
    if current_sum > K:
        return 0
    
    # 가능한 경우라면 1, 아니면 0 반환
    if idx > N:
        if current_sum == K:
            return 1
        else:
            return 0 
    

    take = sol(idx+1, current_sum + idx)
    skip = sol(idx+1, current_sum)

    # 여기에서 지금까지 들어갔다 나왔을 때, 가능한 경우들의 합을 기억해둠
    memo[(idx,current_sum)] = take + skip
    return memo[(idx,current_sum)]

T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    
    memo  = {}

    result = sol(1,0)

    print(f"#{test_case} {result}")