k=int(input())
for j in range(1,k+1):
 num=str(j)
 toggle=False
 for i in range(len(num)):  
    if int(num[i])%3 == 0 and int(num[i])!=0:
        print('X', end=" ")
        toggle=True
    if i == len(num)-1 and toggle!=True:
        print(num, end=" ")