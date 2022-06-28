n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
b=[]
for i in a:
    if(a.count(i)==k and i not in b):
        c+=1
        b+=[i]
        print(i,end=' ')
if(c==0):
    print('-1')