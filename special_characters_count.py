n=input()
n=n.split()
s='!@#$%^&*()_-[]{};:,./?\|'
c=0
for i in n:
    for j in i:
        if j in s:
            c+=1
print(c)