for _ in range(int(input())):
    q=int(input())
    s,i=0,0
    while q:
        r=q%10
        s+=r*(2**i)
        q=q//10
        i+=1
    print(s)
        