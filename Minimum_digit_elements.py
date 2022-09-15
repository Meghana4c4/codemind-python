n=int(input())
l=list(map(int,input().split()))
m=len(str(min(l)))
c=0
for i in l:
    if len(str(i))==m:
        c+=1
print(c)