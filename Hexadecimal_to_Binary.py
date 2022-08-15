for _ in range(int(input())):
    q=int(input(),16)
    q=str(bin(q)[2:])
    c=(((len(q)//4)+1)*4)
    if len(q)%4!=0:
        print(q.zfill(c))
    else:
        print(q)
