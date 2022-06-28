a=input()
b=a.split()
c=[]
for i in b:
    p=str(i)
    q=len(p)
    c+=[q]
s=min(c)
print(s)