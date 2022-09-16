n=input()
n=n.split()
m=[]
for i in n:
    a=min(i)
    b=max(i)
    m.append(a)
    m.append(b)
print(*m)