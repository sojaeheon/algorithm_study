def sort_r(arr):
    new_arr = []
    max_len = 0
    for row in arr:
        num_cnt = {}
        for num in row:
            if num == 0:
                continue
            num_cnt[num] = num_cnt.get(num, 0) + 1

        sort_num = sorted(num_cnt.items(), key=lambda x: (x[1], x[0]))

        new_row = []
        for k, v in sort_num:
            new_row.extend([k, v])

        new_row = new_row[:100]  # 길이 제한
        new_arr.append(new_row)
        max_len = max(max_len, len(new_row))

    for row in new_arr:
        row.extend([0] * (max_len - len(row)))
    return new_arr


def sort_c(arr):
    rows, cols = len(arr), len(arr[0])
    new_arr = [[0] * cols for _ in range(0)]  # 나중에 append
    max_len = 0
    cols_result = []

    for c in range(cols):
        num_cnt = {}
        for r in range(rows):
            if arr[r][c] == 0:
                continue
            num_cnt[arr[r][c]] = num_cnt.get(arr[r][c], 0) + 1

        sort_num = sorted(num_cnt.items(), key=lambda x: (x[1], x[0]))

        new_col = []
        for k, v in sort_num:
            new_col.extend([k, v])

        new_col = new_col[:100]
        cols_result.append(new_col)
        max_len = max(max_len, len(new_col))

    # 이제 결과를 행렬로 다시 만들기
    new_arr = [[0] * cols for _ in range(max_len)]
    for c in range(cols):
        for r in range(len(cols_result[c])):
            new_arr[r][c] = cols_result[c][r]

    return new_arr


# 입력
r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

count = 0

while count <= 100:
    if 0 <= r - 1 < len(arr) and 0 <= c - 1 < len(arr[0]) and arr[r - 1][c - 1] == k:
        break

    if len(arr) >= len(arr[0]):  # R 연산
        arr = sort_r(arr)
    else:  # C 연산
        arr = sort_c(arr)

    count += 1

if count > 100:
    print(-1)
else:
    print(count)
