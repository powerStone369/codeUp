n=int(input())
list=list(input().split(' '))
newList=[]
for i in range(n):
    newList.append(int(list[i]))

for i in range(n):
    print(newList[-(i+1)], end=" ")