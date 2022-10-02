r,c=map(int,input().split())
l=[]
r_sum=0
o_sum=0
for i in range(r):
    m=list(map(int,input().split()))
    l.append(m)
for i in range(len(l)):
    if i%2==0:
        r_sum+=sum(l[i])
    else:
        o_sum+=sum(l[i])
print(r_sum,o_sum)