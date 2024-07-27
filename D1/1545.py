# 거꾸로 출력해 보아요.

T=int(input())

list=list(range(0, T+1))

list.reverse()

print(*list)