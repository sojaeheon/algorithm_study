'''
    진실을 아는 사람이 있는 집합을 빼고 남은 집합 ?
'''


def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
        return parent[x]
    return x


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        parent[root_y] = root_x


# N: 사람의 수, M: 파티의 수
N, M = map(int, input().split())
num, *true_list = map(int, input().split())

# 데이터 받기
data = [[0]]
for _ in range(M):
    num, *lst = map(int, input().split())
    data.append(lst)

# parent 노드 기록
parent = [v for v in range(N + 1)]

for dt in data[1:]:
    # 만약, 1보다 크면 union 진행
    if len(dt) > 1:
        # 기준 점 정하기 : 앞에 나온 값으로
        temp = dt[0]
        for i in dt[1:]:
            union(temp, i)


# 진실인 사람 루트 노드 찾기
true_root = set()
for tr in true_list:
    root = find_set(tr)
    true_root.add(root)

# 거짓말 할 수 있는 그룹 찾기
ans = 0
# 진실을 아는 사람의 수가 0이면, 파티 수가 정답
if not true_list:
    print(M)
else:
    # 데이터 순회(각 파티 순회)
    for dt in data[1:]:
        # 플래그 기본 값
        can_lie = True
        # 각 파티 내 사람들 순회
        for num in dt:
            # 만약 현재 파티원의 부모가 진실노드에 있다면
            if find_set(num) in true_root:
                # 거짓말 할 수 없음
                can_lie = False
                break
        # 거짓말 할 수 있을 때만,
        if can_lie:
            ans += 1
    print(ans)



