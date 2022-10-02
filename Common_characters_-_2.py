n=input().lower().split()
a=0
for d in n[0]:
    c=0
    for i in range(1,len(n)):
        if d in n[i]:
            c+=1
    if c==len(n)-1:
        a+=1
print(a)   