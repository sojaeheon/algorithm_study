def sol (x,y):
    
    end_x, end_y = 0,0
    flag = False

    for i in range(x,n):
        for j in range(y,n):
            if (matrix[i][j] == 0) and j == y:
                flag = True
            elif matrix[i][j] == 0:
                break
            elif matrix[i][j] != 0:
                visited[i][j] = True
                end_x = i+1
                end_y = j+1
        if flag:
            break
            

    return (end_x-x, end_y-y)


T = int(input())


for test_case in range(1,T+1):
    n = int(input())

    matrix = [list(map(int,input().split())) for _ in range(n)]

    visited = [[False] *n for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if (matrix[i][j] != 0) and not visited[i][j]:
                result.append(sol(i,j))

    result.sort(key=lambda x:(x[0]*x[1],x[0]))

    print(f"#{test_case} {len(result)}", end = " ")
    for i in range(len(result)):
        for j in range(2):
            print(result[i][j], end=" ")
        
    print()
