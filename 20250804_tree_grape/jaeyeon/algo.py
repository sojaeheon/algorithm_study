# 노드의 개수 입력 
N = int(input())

# 부모 주어짐. 없으면 -1
parent_list = list(map(int,input().split()))

#삭제할 노드 입력받기
del_node = int(input())

p,c = parent_list.index(parent_list[0]), parent_list[0]

# 노드 인접 리스트 생성
node_list = {}
for child, par in enumerate(parent_list):
    if par == -1:
        root = child
    else:
        node_list.setdefault(par, []).append(child)




print(node_list)