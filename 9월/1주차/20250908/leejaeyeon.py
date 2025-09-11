'''
일정액을 내면 정해진 박스가 가득 찰 때까지 물건 담을 수 있는 해피박스 이벤트
남은 물건의 크기와 가격이 주어짐 
A가 담을 수 있는 최대 물건 가격

상품 개수 : 최대 20
박스 크기 : 최대 100 
python 2초
완전탐색 가능한가
조합
'''
# dp로 풀기
def knapsack(items, capacity):
    dp = [0] * (capacity +1)

    for size, price in items:
        for c in range(capacity , size -1, -1):
            dp[c] = max(dp[c], dp[c-size]+price)
    return dp[-1]

T = int(input())


for test_case in range(1, T+1):
    # A 박스의 크기, 상품의 개수
    N, M = map(int,input().split())
    box_list = []
    for i in range(M):
        # 물건 크기 및 가격
        size, price = map(int,input().split())
        box_list.append([size,price])
    
    result = knapsack(box_list, N)

    print(f"#{test_case} {result}")