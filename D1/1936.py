# 1대1 가위바위보

a, b=map(int, input().split())

if (a==3 and b==2) or (a==3 or b==1) or (a==1 or b==3):
    print('A')
else:
    print('B')