# 홀수만 더하기

T=int(input())

for test_case in range(1, T+1):

    numbers=list(map(int, input().split()))

    numbers_odd=[]

    for number in numbers:
        
        if number%2==0:
            pass
        else:
            numbers_odd.append(number)
    
    odd=sum(numbers_odd)

    print(f'#{test_case} {odd}')