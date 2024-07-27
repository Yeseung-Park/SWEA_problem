# 몫과 나머지 출력하기

T=int(input())

for test_cast in range(1, T+1):

    a, b=map(int, input().split())

    quotient=a//b
    remainder=a%b

    print(f'#{test_cast} {quotient} {remainder}')

