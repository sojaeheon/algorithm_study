n, m = map(int,input().split())

# num과 그 뒤 값들은 리스트에 저장
num , *true_people = map(int,input().split())

# true_people : 진실을 알고있는 사람들의 번호
true_people = set(true_people)

# party에 참석한 번호 저장 리스트
party_list = []

# m개의 파티만큼 순회하며 저장
for i in range(m):
    n, *n_list = map(int,input().split())
    party_list.append(set(n_list))


# m개만큼 순회하며, party_list에 intersection(교집합)으로 추가되는 번호 있으면 진실 리스트에 추가
for _ in range(m):
    for node in party_list:
        if node.intersection(true_people):
            true_people.update(node)
            
# 결과 값 저장 변수
cnt = 0
# 파티리스트를 순회하며 true_people에 없는 리스트를 가진 파티만 값 추가
for party in party_list:
    if not party.intersection(true_people):
        cnt += 1

print(cnt)