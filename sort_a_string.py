n=input()
l=sorted(list(n))
k='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
m=[]
a=0
for i in l:
    if i in k:
        m.append(i)
for i in range(len(n)):
    n=list(n)
    if n[i] in k:
        n[i]=m[a]
        a+=1
p=''.join(n)
print(p)