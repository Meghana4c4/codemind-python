n=input()
n=n.split()
c=[]
for i in n:
    j=ord(max(i))
    k=ord(min(i))
    c.append(abs(j-k))
print(*c)