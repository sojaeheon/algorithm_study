def solve(x, y):
    start_y = y
    start_x = x
    end_x = end_y = 0
    flag = False

    #우선 화약있다니까 함 살펴보자
    #시작 좌표부터 끝까지 샆펴보쟈
    for i in range(start_x, n): #
        for j in range(start_y, n):
            #(1)걍 첨부터보는데 화약도 없고,,, 우선 col이 시작좌표면 break
            # 이 구역은 살펴봤다는 의미
            if data[i][j] ==0 and j == start_y: 
                flag = True
                break
            #(2) 확장중인데... 0이면 더 탐색할 필요가 없음 - 화약이 없다
            elif data[i][j]==0: 
                break
            #(3) 0이 아니다 = 화약이 있다
            elif data[i][j] != 0: 
                data[i][j] = 0 #0으로 바꿔주고 - 나중에 다시 안살펴보게
                end_x, end_y = i+1, i+j #인지범위를 넓혀줌
                continue

        #flag가 True면 break한다
        if flag: 
            #왜 flag가 True면 멈추지.? -이 구역은 탐색했다는 의미
            break

    #구한 구역의 크기 구하기
    ans_x = end_x - start_x
    ans_y = end_x - start_y

    return (ans_x, ans_y)



T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    data = [list(map(int, input().strip().split())) for _ in range(N)]
    result = []
    a = b = 0

    for i in range(n):
        for j in range(n):
            if data[i][j] != 0:
                x, y = solve(i, j)
                result.append( (x,y) )


    #작은 크기순으로 출력해야함
    result.sort(key=lambda item: (item[0] * item[1], item[0]))

    string_list = []

    #중첩 for문으로 모든 숫자를 순회함
    for tup in result:
        for num in tup:
            #각 숫자를 문자열로 변환해서 리스트에 추가
            string_list.append(str(num))

    print(f'#{tc} {len(result)} {" ".join(string_list)}')