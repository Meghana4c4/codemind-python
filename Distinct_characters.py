n=input()
l=list(n.lower())
l1=[]
for i in range(len(l)):
    if l[i]!=' ':
        if l[i] not in l1:
            l1.append(l[i])
            
l1.sort()        
print(''.join(l1))