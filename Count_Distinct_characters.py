n=input()
b=[]
for i in n:
    if i not in b and i not in ' ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        b+=[i]
print(len(b))