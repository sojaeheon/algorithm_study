
# 삭제할 부모 노드에 자식들 지우기
def delete(idx):
    # 부모의 자식 리스트에서 삭제할 노드 제거
    for i in range(n):
        if idx in children[i]:
            children[i].remove(idx)

    stack = [idx]
    # 스택안에 있는 자식들을 부모로하는 자식들 지우기
    while stack:
        next_idx = stack.pop()
        next_node = children[next_idx]

        if next_node:
            for _ in range(len(next_node)):
                stack.append(next_node.pop())
        



n = int(input())
parents = list(map(int,input().strip().split()))
del_node = int(input())

children = [[] for _ in range(n)]   # 각 노드의 자식 리스트 초기화
root = -1   # 루트 노드를 저장할 변수


# 부모에 자식 추가
for i in range(n):
    p = parents[i]
    if p == -1:
        root = i    # 루트노드 찾기
    else:
        children[p].append(i)


delete(del_node)
print(children)

count = 0

for child in children:
    for c in child:
        if not children[c]:
            count+=1

print(count)