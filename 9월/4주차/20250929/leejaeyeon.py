'''
시험 감독

N개의 시험장 시험장별 A명
총감독관, 부감독관 두 종류
총감독관 : 한 시험장에 감시할 수 있는 응시자 수 B명, 
부감독관 : 한 시험장에 감시할 수 있는 응시자 수 C명 
감독관 수의 최솟값 구하기

각 시험장에 총감독관 오직 1명, 부감독관 여러 명 가능
미리 값을 구해두고 넣으면 더 빠르려나

'''

N = int(input())

A_list = list(map(int,input().split()))

B, C = map(int,input().split())
result = 0

for A in A_list:
    result += 1 
    if (A-B) >0:
        result += (A-B+C-1)//C
print(result)