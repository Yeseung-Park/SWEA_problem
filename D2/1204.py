# [S/W 문제해결 기본] 1일차 - 최빈수 구하기

T=int(input())

for test_case in range(1, T+1):

    test_number=int(input())

    scores=list(map(int, input().split()))

    num_dict={}

    for i in range(len(scores)):
        num=0

        for j in range(len(scores)):

            if scores[i]==scores[j]:

                num+=1

        num_dict[scores[i]]=num
    
    for key in num_dict:

        if num_dict[key]==max(num_dict.values()):

            print(f'#{test_number} {key}')


