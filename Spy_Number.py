num=int(input())
s=0
p=1
num1=num
while(num>0):
    d=num%10
    s=s+d
    p=p*d
    num=num//10
if(s==p):
    print('Spy Number')
else:
    print('Not Spy Number')