'''
원소의 합이 k개인 경우의 수 m을 알고싶다. 
이때 숫자들은 1~n 사이의 수이다. 
'''

def sol(idx, current_sum):
    #이미 다녀간 곳이면 pass
    if (idx, current_sum) in memori:
        return memori[(idx, current_sum)]
    
    #가지치기 
    if current_sum > k:
        return 0
    
    if idx > n:
        if current_sum == k:
            return 1
        else: 
            return 0
        

    take = sol(idx+1, current_sum+idx)
    skip = sol(idx+1, current_sum)

    #여기에서 지금까지 들어갔다 나왔을 때, 가능한 경우들의 합을 기억하자
    memori[ (idx, current_sum) ] = take + skip
    return memori[ ((idx, current_sum)) ]

t = int(input())

for tc in range(1, t+1):
    #총숫자 n, 원소의 합 k
    n, k = map(int, input().split())

    memori = {}

    result = sol(1,0)

    print(f'#{tc} {result}')