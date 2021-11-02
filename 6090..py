a,m,d,n=map(int,input().split())

def function(n):
    if n==1:
        return a
    else:
        return function(n-1)*m+d

print(function(n))