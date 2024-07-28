# 큰 놈, 작은 놈, 같은 놈

T=int(input())

for test_case in range(1, T+1):

    a, b=map(int, input().split())

    if a<b:
        print(f'#{test_case} <')
    elif a==b:
        print(f'#{test_case} =')
    elif a>b:
        print(f'#{test_case} >')