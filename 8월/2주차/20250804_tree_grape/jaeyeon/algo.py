# 노드의 개수 입력 
N = int(input())

# 부모 주어짐. 없으면 -1
parent_list = list(map(int,input().split()))


#삭제할 노드 입력받기
del_node = int(input())

tree_list = [[] for _ in range(N)]
root = -1

for i,p in enumerate(parent_list):
    if p == -1:
        root = i
    else:
        tree_list[p].append(i)

if del_node == root:
    print(0)

else:
    tree_list[parent_list[del_node]].remove(del_node)

    cnt = 0
    for i in range(N):
        tmp = i
        del_subtree = False
        while tmp != -1:
            if tmp == del_node:
                del_subtree = True
                break
            tmp = parent_list[tmp]
        if not del_subtree and not tree_list[i]:
            cnt += 1
    print(cnt)