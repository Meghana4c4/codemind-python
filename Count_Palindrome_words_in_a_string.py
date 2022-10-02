def palin(n):
    n=n.lower()
    l=n[::-1]
    if n==l:
        return True
    else:
        return False
n=input()
l=n.split()
c=0
for i in l:
    if palin(i)==True:
        c+=1
print(c)