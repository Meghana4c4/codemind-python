def fun(n):
    return n[::-1]
s=input()
s=s.split()
for i in range(len(s)):
    if i%2==0:
        s[i]=fun(s[i])
        
print(*s)