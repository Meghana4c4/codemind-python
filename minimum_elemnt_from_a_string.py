n=input()
n=n.split()
n=n[len(n)-1]
for i in sorted(n):
    if i!=' ':
        if i.lower() in sorted(n):
            print(i.lower())
        else:
            print(i)
        break
            