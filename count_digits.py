n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i<0:
        i=str(i)
        print(len(i)-1,end=' ')
    else:
        i=str(i)
        print(len(i),end=' ')