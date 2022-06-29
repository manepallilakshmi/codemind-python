n=input()
n1=n.lower()
x=n1.split()
for i in x:
    if i==i[: : -1]:
        print('True')
    else:
        print('False')