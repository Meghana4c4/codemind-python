s1=list(input().lower())
s2=list(input().lower())
l=[]
for i in s1:
    for j in s2:
        if i==j:
            if i not in l:
                l.append(i)
                
for k in l:
    if k==' ':
        l.remove(' ')
        l.sort()
else:
    l.sort()
if len(l)!=0:
    print(''.join(l))
else:
    print(-1)