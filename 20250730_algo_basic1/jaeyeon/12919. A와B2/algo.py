
# 입력
S = list(input())
T = list(input())

# T -> S 가능 여부 함수
def find_s(T):
    if T == S:
        return 1

    # S와 달라 마지막까지 전부 제거된 경우
    if len(T) == 0:
        return 0

    result = 0
    # 맨 뒷글자가 A인 경우
    if T[-1] == 'A':
        # 맨 뒷글자인 A 삭제 후 재귀
        result = result or find_s(T[:-1])

    # 맨 앞글자가 B인 경우
    if T[0] == 'B':
        # 맨 앞글자 제거하고 뒤집어서 재귀
        result = result or find_s(T[1:][::-1])
    return result
        
    
print(find_s(T))