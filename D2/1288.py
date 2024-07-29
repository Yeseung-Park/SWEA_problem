# 새로운 불면증 치료법 (미완성)

T=int(input())

for test_case in range(1, T+1):

    N=int(input())

    appeared_number=set()

    i=1

    is_number_full=False

    while is_number_full==False:

        N=N*i

        string=str(N)

        for num in string:

            appeared_number.add(int(num))

        if appeared_number==(0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
            is_number_full=True

        i+=1

        
    
    print(f'#{test_case} {i}')

        

        
