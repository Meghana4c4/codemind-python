n=input()
l=list(n.lower())
l1=[]
for i in range(len(l)):
    if l[i]!=' ':
        if l.count(l[i])==1:
            l1.append(l[i])

m=''.join(sorted(l1))
print(m)

