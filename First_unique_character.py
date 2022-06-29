n=input()
x=list(n)
c=0
for i in x:
    if  i in 'abcdefghijklmnopqrstuvwxyz' and x.count(i)==1:
        c+=1
        print(i)
        break
if(c==0):
    print('-1')