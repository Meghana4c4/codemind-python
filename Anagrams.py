n=input().lower()
m=input().lower()
n=set(sorted(list(n)))
m=set(sorted(list(m)))
if n==m:
    print('True')
else:
    print('False')