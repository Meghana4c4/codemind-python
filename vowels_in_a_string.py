n=input()
k=input()
for i in n:
    if i==k:
        b=(True)
        m=n.index(k)
        break
    else:
        b=False
if b:
    print(b)
    print(m)
else:
    print(b)
    