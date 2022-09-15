def palin(n):
    n=str(n)
    if len(n)==1:
        return True
    for i in range(len(n)//2):
        if n[i]==n[len(n)-i-1]:
            return True
        return False
n=int(input())
l=list(map(int,input().split()))
c=0

for i in l:
    if palin(i):
        c+=1
print(c)