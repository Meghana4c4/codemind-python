n=input()
vow='aeiouAEIOU'
c=[]
k=[]
v=[]
n=n.split()
for i in n:
    for j in i:
        if j in vow:
            c.append(j)
c=set(c)
for i in c:
    if i.islower():
        k.append(i)
    else:
        v.append(i)
if len(k)==5 or len(v)==5:
    print(True)
else:
    print(False)