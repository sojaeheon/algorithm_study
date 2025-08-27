
# S를 T로 바꿀 수 있는 지 학인하는 함수
def s_to_t(s, t):

    # T문자가 S문자 수랑 같아졌을때 비교후 True, False 반환
    if len(s) == len(t):
        return s == t
    
    # T를 앞에서부터 꺼냈을 때, A문자이면 그대로 재귀, B문자이면 뒤집어서 재귀함수 호출
    check = False
    if t[-1] == "A" :
        check =  s_to_t(s,t[:-1])
        if check: return True
    if t[0] == "B":
        check = s_to_t(s,t[::-1][:-1])
        if check : return True
    return False


# S와 T 입력 받기
S = input().strip()
T = input().strip()

# S를 T로 바꿀 수 있는 지 확인 후 True이면 1, False이면 0으로 반환
result = 1 if s_to_t(S,T) else 0

print(result)

