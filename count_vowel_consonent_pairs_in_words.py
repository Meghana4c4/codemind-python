n=input()
n=n.split()
c=0
vow='AEIOUaeiou'

for i in n:
    a,b=0,len(i)-1
    while (a<b and a!=b):
        if (i[a] in vow and i[b] not in vow):
            c+=1
        elif (i[a] not in vow and i[b] in vow):
            c+=1
        a+=1
        b-=1
print(c)