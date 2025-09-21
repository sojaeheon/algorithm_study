'''
연산자 끼워넣기

최댓값, 최솟값 구하기
전체 경우의 수 구하고 정렬해서 최소, 최대

'''

def dfs(idx, current):

    if idx == n:
        result.add(current)
        return
    num = num_list[idx]
    if op_list[0] > 0:
        op_list[0] -= 1
        dfs(idx+1, current + num)
        op_list[0] += 1
    if op_list[1] > 0:
        op_list[1] -= 1
        dfs(idx+1, current - num)
        op_list[1] += 1
    if op_list[2] > 0:
        op_list[2] -= 1
        dfs(idx+1, current * num)
        op_list[2] += 1
    if op_list[3] > 0 :
        op_list[3] -= 1
        div = abs(current) // abs(num)
        if (current > 0 and num <0) or (current < 0 and num > 0):
            div = -div 
        dfs(idx+1, div)
        op_list[3] += 1
    


n = int(input())

num_list = list(map(int,input().split()))

op_list = list(map(int,input().split()))
result = set()

dfs(1,num_list[0])


print(max(result))
print(min(result))