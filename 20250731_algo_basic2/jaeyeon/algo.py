n = int(input())

eggs = []
for i in range(n):
    durability , weight = map(int, input().split())

    eggs.append([durability,weight])
    
result = 0  
idx = 0


# 다시풀어보기