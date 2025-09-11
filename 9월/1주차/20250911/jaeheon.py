# 매일 칭찬할 일이 있을 때마다 원생에게 1달란트 스티커를 나눠 주는데,
# 달란트 시장에서 1년동안 모은 달란트만큼 사탕으로 교환해 주기로 했다.
# 10개를 3묶음으로 나누어서 각 묶음의 곱의 개수로 사탕을 교한해주기로 했다.

# 제약사항
# 10 <= N <= 100
# 묶음의 수 p <= N

# def calculator(remain,count,lst):
#     global result
#     current_lst = lst[:]
#     if n <= 0: return

#     if count == p-1:
#         mul = 1
#         for i in lst:
#             mul*=i
#         result = max(result,mul*remain)
#         return
    
#     for i in range(remain,0,-1):
#         current_lst.append(i)
#         calculator(remain-i,count+1,current_lst)
#         current_lst.pop()
    

# T = int(input())

# for tc in range(1,T+1):
#     n,p = map(int,input().split())
#     result = 0
    
#     calculator(n,0,[])
#     print(f'#{tc} {result}')

T = int(input())
for tc in range(1, T+1):
    n, p = map(int, input().split())
    q, r = n//p, n%p
    print(q,r)
    result = pow(q, p-r) * pow(q+1, r)
    print(f'#{tc} {result}')
