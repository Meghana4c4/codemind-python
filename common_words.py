s1=input().lower().split()
s2=input().lower().split()
l=[]
for i in s2:
    for j in s1:
        if i==j:
            l.append(i)
print(*l)