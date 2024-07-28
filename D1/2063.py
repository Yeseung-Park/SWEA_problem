# 중간값 찾기

N=int(input())

if N%2==0:
    print('홀수를 입력하세요')

    N=int(input())

scores=list(map(int, input().split()))

scores.sort()

print(scores[N//2])