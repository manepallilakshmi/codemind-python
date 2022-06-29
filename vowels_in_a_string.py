n=input()
k=input()
for i in n:
    if k in n:
        print('True')
        print(n.index(k))
        break
    else:
        print('False')
        break