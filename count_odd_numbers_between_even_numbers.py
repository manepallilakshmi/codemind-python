n=int(input())
a=list(map(int,input().split()))
co=0
for i in range(0,n):
    if a[i]%2==0:
        c=i
        break
for j in range(n-1,-1,-1):
    if a[j]%2==0:
        d=j
        break
for k in range(c+1,d):
    if a[k]%2!=0:
        co+=1
print(co)