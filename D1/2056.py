# 연월일 달력

T=int(input())
 
for test_case in range(1,T+1):
 
    date=str(input())
 
    year=date[0:4]
    month=date[4:6]
    day=date[6:]
 
    day_31_month=[1, 3, 5, 7, 8, 10, 12]
    day_30_month=[4, 6, 9, 11]
            
    if int(month) in day_31_month:
        if int(day)<=31:
            print(f'#{test_case} {year}/{month}/{day}')
        else:
            print(f'#{test_case}', -1)
    elif int(month)==2:
        if int(day)<=28:
            print(f'#{test_case} {year}/{month}/{day}')
        else:
            print(f'#{test_case}', -1)
    elif int(month) in day_30_month:
        if int(day)<=30:
            print(f'#{test_case} {year}/{month}/{day}')
        else:
            print(f'#{test_case}', -1)
    else:
        print(f'#{test_case}', -1)