n=input()
b=[]
for i in n:
    if i not in b and i not in ' ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        b+=[i]
p=sorted(b)
for j in p:
    print(j,end='')