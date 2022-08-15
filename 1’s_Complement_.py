n=str(bin(int(input())))
n=n[2:]
d={'0':'1','1':'0'}
s=0
l=[]
for i in n:
    l.append(d[i])
l.reverse()
for i in range(len(l)):
    s+=int(l[i])*(2**i)
print(s)
    