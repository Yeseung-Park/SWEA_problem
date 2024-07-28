# 최대수 구하기

T=int(input())

for test_case in range(1, T+1):

    numbers=list(map(int, input().split()))

    for i in range(0,len(numbers)-1):

        if numbers[i]<=numbers[i+1]:
            pass
        elif numbers[i]>numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        
    print(f'#{test_case} {numbers[len(numbers)-1]}')
