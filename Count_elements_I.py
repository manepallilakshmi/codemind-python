n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
p=0
for i in a:
    if(i in b and i not in c):
        c+=[i]
        p+=1
print(p)