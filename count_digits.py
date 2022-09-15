n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    c.append(len(str(abs(i))))
print(*c)    