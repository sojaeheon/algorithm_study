t = int(input())

for tc in range(1, t+1):
    #달란트개수n, 묶음개수p
    n, p = map(int, input().split())

    num = n//p #나눈 몫을 구한다
    remain = n%p #나머지를 구한다
    num_list = [num]* p #p개의 칸에 다 num을 넣어주고

    result = 1


    for i in range(remain):
        num_list[i] +=1
    
    for i in num_list:
        result *= i

    print(f'#{tc} {result}')

