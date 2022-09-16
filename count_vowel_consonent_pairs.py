n=input()
c=0
vow='AEIOUaeiou'
i,j=0,len(n)-1
while i!=j and i<j:
    if n[i]!=' ' and n[j]!=' ':
        if n[i] in vow and n[j] not in vow:
            c+=1
        elif n[i] not in vow and n[j] in vow:
            c+=1
    i+=1
    j-=1
print(c)