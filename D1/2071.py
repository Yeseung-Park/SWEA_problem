# 평균값 구하기

T=int(input())

for test_case in range(1, T+1):

    numbers=list(map(int, input().split()))

    numbers_sum=sum(numbers)

    average=round(numbers_sum/len(numbers))

    print(f'#{test_case} {average}')
