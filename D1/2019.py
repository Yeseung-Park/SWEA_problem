# 더블더블

T = int(input())

list=[]

for i in range(0,T+1):
    num=2

    num**=i

    list.append(num)

print(*list)