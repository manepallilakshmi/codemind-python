n=int(input())
a=list(map(int,input().split()))
b=[]
s=0
for i in a:
    if i%2==0 and i not in b:
        b+=[i]
        s+=i
print(s)