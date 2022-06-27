n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
co=0
for i in a:
    if(i<b or i>c):
        co+=1
        print(i,end=' ')
if(co==0):
    print('-1')