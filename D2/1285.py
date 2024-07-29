# 아름이의 돌 던지기 (원래는 C++만 되는 문제)

T=int(input())

for test_case in range(1, T+1):

    N=int(input())

    distance=list(map(int, input().split()))

    difference=[]

    for dist in distance:

        difference.append(abs(dist-0))

    for i in range(len(difference)-1, 0, -1):
        for j in range(0, i):
            if difference[j]>difference[j+1]:
                difference[j], difference[j+1] = difference[j+1], difference[j]
    
    result=difference[0]

    num=0

    for val in difference:
        if val==result:
            num+=1
    
    print(f'#{test_case} {result} {num}')