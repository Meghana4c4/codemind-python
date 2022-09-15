n=input()
n=n.split()
vow='aeiou'
c=[]
k=[]
for i in n:
    for j in i:
        if j in vow:
            c.append(j)
c=set(c)
for i in vow:
    if i not in c:
        k.append(i)
if len(k)!=0:
    print(*k)
else:
    print(0)