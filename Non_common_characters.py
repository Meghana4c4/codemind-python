s1=list(input().lower())
s2=list(input().lower())
s=""
l=[]
c=0
for i in s1:
    if i not in s2 and i not in s and i!=" ":
        s+=i
        if i not in l:
            l.append(i)
            c+=1
for i in s2:
    if i not in s1 and i not in s and i!=" ":
        s+=i
        if i not in l:
            l.append(i)
            c+=1
print(c)