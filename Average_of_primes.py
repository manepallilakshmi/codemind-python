n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in a:
    if i!=1:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            s=s+i
            c+=1
print("%0.2f"%(s/c))