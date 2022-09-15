n=input()
n=n.split()
c=0
vow='AEIOUaeiou'
for i in n:
    for j in i:
        if j in vow:
            c+=1
print(c)