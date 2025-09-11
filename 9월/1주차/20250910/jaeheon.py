# 3 가지 사항
# 1. 화학 물질이 담긴 용기들이 사각형을 이루고 있다. 또한, 사각형 내부에는 빈 용기가 없다
# 2. 화학 물질이 담긴 용기들로 이루어진 사각형들은 각각 차원(가로의 용기수 x 세로의 용기수)이 다르다.
# 3. 2개의 화학 물질이 담긴 용기들로 이루어진 사각형들 사이에는 빈 용기들이 있다.

# 제약사항
# n <= 100

# 출력
# 각 테스트 케이스 각각에 대한 답 출력,
# 각 테스트 케이스에 주어진 행렬에서 추출된 부분행렬들을 개수와 그 뒤를 이어 행렬들의 행과 열의 크기를 출력한다
# 크기는 행과 열을 곱한 값으로, 크기가 작은 순서대로 출력한다

import heapq

def find_row_col(arr, row,col):

    c_count = 1
    r_count = 1
    
    next_row = row
    while arr[next_row][col] != 0:
        next_col = col
        
        while arr[next_row][next_col] != 0: 
            if next_row == row:   
                c_count+=1
            arr[next_row][next_col] = 0
            next_col +=1
            if not (0<= next_col <n): break
        
        r_count +=1
        next_row+=1
        if not (0<= next_row <n): break
    
    return r_count-1,c_count-1,(r_count-1)*(c_count-1)


T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    result = []
    count = 0
    for row in range(n):
        for col in range(n):
            if arr[row][col] > 0:
                r_row, r_col, r_sum = find_row_col(arr, row,col)
                heapq.heappush(result, (r_sum,r_row,r_col))
                count+=1  
    
    print(f'#{tc} {count}',end=' ')
    for _ in range(count):
        a ,b,c = heapq.heappop(result)
        print(f'{b} {c}',end=' ')
    print()
