def sortStr(S):
    N = len(S)
    temp = ""
    for i in range(N):
        if (S[i] != 'a' and S[i] != 'e' and S[i] != 'i'
                and S[i] != 'o'and S[i] != 'u'):
            temp += S[i]
    if (len(temp)):
        p = list(temp)
        p.sort()
        temp=''.join(p)
    ptr = 0
    for i in range(N):
      S = list(S)
      if (S[i] != 'a' and S[i] != 'e' and S[i] != 'i'
                and S[i] != 'o' and S[i] != 'u'):
            S[i] = temp[ptr]
            ptr += 1
    m=(''.join(S))
    return m
S = input()
S=S.split()
c=[]
for i in S:
    c.append(sortStr(i))
print(*c)




 