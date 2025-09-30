# N 개의 시험장
# i번 시험장에 있는 응시자의 수 Ai명
# 총 감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명
# 부 감독관은 한 시험장에서 감시할 수 있는 응시자의 수 C명

# 각 시험장에 총감독관은 오직 1명만 있어야 하고, 부 감독관은 여러명 있어도 된다
# 각 시험장마다 응시생들을 모두 감시해야한다
# 이때, 필요한 감독관 수의 최솟값을 구하는 프로그램 작성

n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())

count = 0

for i in a:
    if i == 0: continue
    current_num = i - b
    count+=1

    if current_num > 0:
        num = current_num//c
        count += num
        num_1 = current_num%c
        
        if num_1>0:
            count+=1

print(count)
    

