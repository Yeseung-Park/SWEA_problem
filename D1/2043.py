# 서랍의 비밀번호

P, K=map(int, input().split())

if P>K:
    print(P-K+1)
elif P==K:
    print(0)
elif P<K:
    print(1000-K+P)

