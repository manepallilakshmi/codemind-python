n=int(input())
a=0
b=1
l=[0,1]
for i in range(2,n):
    c=a+b
    l+=[c]
    a=b
    b=c
if(n in l):
    print('True')
else:
    print('False')