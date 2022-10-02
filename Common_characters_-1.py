n=input().lower().split()
a=1
for d in n[0]:
    c=0
    for i in range(1,len(n)):
        if d in n[i]:
            c+=1
    if c==len(n)-1:
        print(d,end='')
        a=0
if a:
    print('-1')