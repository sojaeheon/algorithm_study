N = int(input()) 
lst = map(int, input().split())

# 정답 리스트 만들기 
ans =[]
stack= []

# 순회하기 
for i, height in enumerate(lst):
    idx = i + 1             # 위치를 표시하므로 1부터 시작  
    
    # stack이 비어 있지 않고, 이전 높이보다 내가 크다면, 전달할 수 없으므로 
    while stack and stack[-1][1] < height:
        # 불필요한 top 제거하기  = 나보다 높은 top만 남기기  
        stack.pop()
    
    # stack이 비어있다면, 
    if not stack:
        # 맨 첫번째이거나, 내가 가장 큰 값이라서 전달하지 못하는 경우임 
        ans.append(0)

    else: 
    # stack이 비어있지 않다면, 해당 요소는 내가 전달할 top
        # 나보다 높고, 근접한 값 
        ans.append(stack[-1][0])
        
    # 다음 비교할 대상 top 추가하기
    stack.append((idx, height))   
     
print(' '.join(map(str,ans)))