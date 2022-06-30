n,m=map(int,input().split())
if(n>m):
    n,m=m,n
c=n
while(c>0):
    if n%c==0 and m%c==0:
        print(c)
        break
    c-=1