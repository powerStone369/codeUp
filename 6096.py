num=19
baduk=[]

for i in range(num):
    baduk.append([])

for i in range(num):
    baduk[i]=[a for a in map(int,input().split(" "))]
    
n=int(input())
locate=[]

for i in range(n):
    locate.append([a for a in map(int,input().split(" "))])

for i in range(n):
    x=locate[i][0]
    y=locate[i][1]

    for j in range(num):
        if baduk[x-1][j] == 0:
            baduk[x-1][j] = 1
        elif baduk[x-1][j] == 1:
            baduk[x-1][j] = 0
        if baduk[j][y-1] == 0:
            baduk[j][y-1] = 1
        elif baduk[j][y-1] == 1:
            baduk[j][y-1] = 0

for i in range(num):
    for j in range(num):
        print(baduk[i][j], end=" ")
    print()


