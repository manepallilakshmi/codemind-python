n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b+=[i]
        print(i,end=' ')
        print(a.count(i),end=' ')