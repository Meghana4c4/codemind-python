n=input()
n=n.split()
vow='AEIOUaeiou'
c=0
for k in n:
    i,j=0,len(k)-1
    if k[i]!=' ' and k[j]!=' ':
        if k[i] in vow and k[j] not in vow:
            c+=1
print(c)