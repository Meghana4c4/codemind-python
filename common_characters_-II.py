s1=list(input().lower())
s2=list(input().lower())
c=0
s=""
for i in s1:
        if i in s2 and i not in s and i!=" ":
            s+=i
            c+=1
print(c)