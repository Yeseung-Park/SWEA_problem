# 알파벳을 숫자로 변환 (미제출)

alphabet=input()

alphabet_list=list(alphabet)

num_list=[]

i=0

for _ in alphabet_list:
    i+=1
    num_list.append(i)

print(*num_list)