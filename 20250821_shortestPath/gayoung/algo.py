'''
    가중치 방향 그래프 g가 양수인 경로가 있는지 없는지 ?
    -> 1, 0 으로 이루어짐 : 모든 방향, 플로이드 워셜
'''


def solve(graph):
    # 모든 정점의 거리 고려
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dik = adj_matrix[i][k]
                dkj = adj_matrix[k][j]
                # k를 거쳐 가는 경로가 있다면,
                if dik > 0 and dkj > 0:
                    adj_matrix[i][j] = 1
    return graph


# N: 정점의 개수
N = int(input())
adj_matrix = []
for _ in range(N):
    adj_matrix.append(list(map(int, input().split())))
result = solve(adj_matrix)
for lst in result:
    print(*lst)