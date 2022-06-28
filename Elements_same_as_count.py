n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in a:
    if(i==a.count(i)and i not in b):
        c+=1
        b+=[i]
        print(i,end=' ')
        
if(c==0):
    print('-1')