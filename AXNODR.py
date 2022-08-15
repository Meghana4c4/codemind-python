def fun(n):
    i=2
    t=1
    while i<=n:
        if i%2==0:
            t=t^i
        else:
            t=t&i
        i+=1    
    return t
for _ in range(int(input())):
    n=int(input())
    print(fun(n))
        