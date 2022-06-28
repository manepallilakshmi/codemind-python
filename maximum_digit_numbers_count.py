n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    i=str(i)
    s=len(i)
    b+=[s]
for j in a:
    j=str(j)
    p=len(j)
    if (p==max(b)):
        print(j,end=' ')