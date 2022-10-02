n=input()
l=list(n.lower())
l1=[]
for i in range(len(l)):
    if l[i]!=' ':
        if l.count(l[i])==1:
            l1.append(l[i])
            break

if len(l1)==0:
    print('-1')
else:
    print(*l1)