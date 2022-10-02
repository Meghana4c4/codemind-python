def palin(n):
    n=n.lower()
    l=n[::-1]
    if n==l:
        return True
    else:
        return False
n=input()
print(palin(n))