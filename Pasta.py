n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(m):
    if b.count(b[i])<=a.count(b[i]):
        print('Yes')
        break
    else:
        print('No')
        break
    
        
        