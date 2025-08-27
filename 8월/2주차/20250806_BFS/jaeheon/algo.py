from collections import deque

d_row = [-1,1,0,0]
d_col = [0,0,-1,1]

def search_bfs(r,c):
    global result,cnt

    visited = [[-1]*m for _ in range(n)]
    que = deque()
    que.append((r,c,1))
    
    visited[r][c] = 0
    max_visit = 0
    while que:

        c_row, c_col, count = que.popleft()
        for i in range(4):

            n_col = c_col + d_col[i]
            n_row = c_row + d_row[i]

            if n_col<0 or n_col>=m or n_row < 0 or n_row >= n:
                continue
            if visited[n_row][n_col] != -1:
                continue
            if arr[n_row][n_col] == 'W':
                continue
            if arr[n_row][n_col] == 'L':
                    visited[n_row][n_col] = count
                    if max_visit <count:
                        max_visit = count
                    que.append((n_row,n_col,count+1))
    return max_visit

n, m = map(int,input().strip().split())
arr = [list(input().strip()) for _ in range(n)]

result = 0

for r in range(n):
    for c in range(m):
        if arr[r][c] == 'L':
            result = max(result,search_bfs(r,c))
print(result)



