n=int(input())
l=list(map(int,input().split()))
for i in range(n-1):
    if l[i]<l[i+1]:
        b='yes'
    else:
        b='no'
        break
print(b)