n=input()
m=[]
n=n.split()
vow='AEIOUaeiou'
c=0
for i in n:
    for j in i:
        if j in vow:
            c+=1
    m.append(c)
    c=0
print(max(m))