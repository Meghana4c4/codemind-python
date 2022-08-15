def Add(x,y):
    if (y == 0):
       return x
    else:
        return Add( x ^ y, (x & y) << 1)
x,y=map(int,input().split())
print(Add(x,y))