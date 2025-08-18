import sys

sys.stdin = open('input.txt', 'r')


# 전위 순회
def front(node):
    # 종료 조건 
    if node not in ddict:
        return

        # 재귀 호출
    left_child = ddict[node][0]
    right_child = ddict[node][1]

    print(node, end='')
    front(left_child)
    front(right_child)


# 중위 순회
def mid(node):
    # 종료 조건 
    if node not in ddict:
        return

        # 재귀 호출
    left_child = ddict[node][0]
    right_child = ddict[node][1]

    mid(left_child)
    print(node, end='')
    mid(right_child)


# 후위 순회
def last(node):
    # 종료 조건 
    if node not in ddict:
        return

        # 재귀 호출
    left_child = ddict[node][0]
    right_child = ddict[node][1]

    last(left_child)
    last(right_child)
    print(node, end='')

N = int(input())
ddict = {}
for _ in range(N):
    key, value1, value2 = input().split()
    ddict[key] = [value1, value2]

front('A')
print()
mid('A')
print()
last('A')
