n=input()
n=n.split()
c=[]
k=[]
vow='aeiouAEIOU'
for i in n:
    for j in i:
        if j in vow:
            c.append(j)
for i in c:
    if i not in k:
        k.append(i)
if len(k)!=0:
    print(*k)
else:
    print(-1)