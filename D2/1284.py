# 수도 요금 경쟁

T=int(input())

for test_case in range(1, T+1):

    P, Q, R, S, W = map(int, input().split())

    A_money=W*P

    if W<=R:
        B_money=Q
    else:
        B_money=Q+(W-R)*S

    if A_money<=B_money:
        print(f'#{test_case} {A_money}')
    else:
        print(f'#{test_case} {B_money}')