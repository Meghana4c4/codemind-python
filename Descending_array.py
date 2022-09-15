n=int(input())
l=list(map(int,input().split()))
i=0
while i<n-1:
    if l[i]>l[i+1]:
        b='yes'
        i+=1
    else:
        b='no'
        break
print(b)
