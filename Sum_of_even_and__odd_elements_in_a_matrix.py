r,c=map(int,input().split())
l=[]
e,o=0,0
for i in range(r):
    m=list(map(int,input().split()))
    l.append(m)

for i in l:
    for j in i:
        if j%2==0:
            e+=j
        else:
            o+=j
print(e,o)