for _ in range(int(input())):
    q=int(input())
    s,i=0,0
    while q:
        n=q%10
        s+=n*(8**i)
        q=q//10
        i+=1
    q=s
    l=[]
    while q:
        r=q%2
        l.append(r)
        q=q//2
    l.reverse()
    print(*l, sep='')