n=int(input())
a=list(map(int,input().split()))
b=[0,1]
for i in a:
    if i not in b:
        print('False')
        break
else:
    print('True')