n=int(input())
k=list(map(int,input().split()))
c=0
d=0
for i in range(0,len(k)-2,2):
    if k[i]<k[i+1] and k[i+1]>k[i+2]:
        c+=1
    elif k[i]>k[i+1] and k[i+1]<k[i+2]:
        c+=1
    else:
        d=1

if d==1:
    print('no')
else:
    print('yes')