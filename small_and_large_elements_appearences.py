n=input()
n=list(n)
n=sorted(n)
m=[]
for i in n:
    if i.strip():
        m.append(i)
print(m[0],m.count(m[0]),m[len(m)-1],m.count(m[len(m)-1]))