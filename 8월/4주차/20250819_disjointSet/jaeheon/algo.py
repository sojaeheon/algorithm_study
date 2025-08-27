
# n 명의 사람들
# 진실을 아는 사람들이 주어진다
# 각 파이테 오는 사람들의 번호가 주어진다
# 파티 개수의 최대값을 구하는 프로그램을 작서하시오


# def find_set_pc(x):
#     if people[x] == x:
#         return x
#     people[x] = find_set_pc(people[x])
#     return people[x]

# def union(x,y):
#     root_x = find_set_pc(x)
#     root_y = find_set_pc(y)
    
#     if root_x != root_y:
#         people[root_y] = root_x


# n,m <= 50
# n 사람의 수, m 파티의 수
n, m = map(int, input().split())
cmd = list(map(int, input().split()))
true_count, true_people = cmd[0], set(cmd[1:]) if cmd[0] else set()

parties = []
for _ in range(m):
    data = list(map(int, input().split()))
    parties.append(data[1:])  # 사람 목록만 저장

# 연쇄 전파: 더 이상 늘어나지 않을 때까지 반복
changed = True
while changed:
    changed = False
    for p in parties:
        # 파티에 진실 아는 사람이 하나라도 있으면, 모두 진실 집합에 편입
        if true_people & set(p):
            before = len(true_people)
            true_people.update(p)
            if len(true_people) > before:
                changed = True

# 거짓말 가능한 파티 카운트
result = 0
for p in parties:
    if not (true_people & set(p)):
        result += 1

print(result)



