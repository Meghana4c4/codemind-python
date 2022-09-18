a=input()
a=a.lower()
a=a.split()
b=input()
b=b.lower()
b=b.split()
c=0
if len(a)>=len(b):
    for i in a:
        for j in b:
            if i==j:
                c+=1
else:
    for i in b:
        for j in a:
            if i==j:
                c+=1
print(c)
    
