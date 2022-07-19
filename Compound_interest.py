p,r,t=map(int,input().split())
A=p*(pow((1+r/100),t))
x="{0:.2f}".format(A)
print(x)