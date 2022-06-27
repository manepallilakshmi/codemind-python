n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i
if(s//n in a):
    print('True')
else:
    print('False')