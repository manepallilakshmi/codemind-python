n=int(input())
a=list(map(int,input().split()))
s=0
b=[]
for i in a:
    if(a.count(i)==1):
        s+=i
    if(a.count(i)>1 and i not in b):
          b+=[i]
          s+=i
print(s)