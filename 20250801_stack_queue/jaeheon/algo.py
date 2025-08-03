def reception(tops,n):
    st = []
    answer = [0]*n
    for i in range(n):
        while st:
            if st[-1][1] >= tops[i]:
                answer[i] = st[-1][0] + 1
                break
            else:
                st.pop()
        st.append((i,tops[i]))
        
    return answer


n = int(input())
tops = list(map(int,input().strip().split()))

result = reception(tops,n)

print(*result)