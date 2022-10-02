n=input()
l=list(n.lower())
l1=[]
c=0
for i in range(len(l)):
    if l[i]!=' ':
        if l.count(l[i])==1:
            l1.append(l[i])
            c+=1

print(c)