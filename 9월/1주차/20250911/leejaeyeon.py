'''
달란트 시장
칭찬 = 1달란트 
10개의 달란트 = 10개를 3묶음으로 나눠서 각 묶음의 곱의 개수로 사탕을 교환해줌
1 x 1 x 8 = 8
3 x 3 x 4 = 36

N <= 100
묶음의 수 : P <= N

10 //3  = 3
20//5 = 4 
4 4 4 4 4

30 // 9 = 3...3
4 4 4 3 3 3 3 3 3

N // P = 몫, 나머지
나머지 개수만큼 몫에 +1




'''

T = int(input())


for test_case in range(1,T+1):
    N, P = map(int,input().split())

    num = N // P
    remain = N % P
    num_list = [num] * (P)
    # print(num_list)
    
    result = 1

    for i in range(remain):
        num_list[i] += 1
    for i in range(len(num_list)):
        result *= num_list[i]
    
    print(f"#{test_case} {result}")