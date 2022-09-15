def rev(n):
   return n[::-1]
s=input()
s=s.split()
for i in range(len(s)):
    s[i]=rev(s[i])
print(*s)
    