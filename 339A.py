n=input()
#print(n)
s=len(n)
#print(s)
f=[]
q=[]
i=0
while i<s:
    if n[i]!='+':
        f.append(int(n[i]))
    i=i+1
f.sort()
#print(f)
k=len(f)
j=0
while j<k:
    q.append(f[j])
    q.append('+')
    j=j+1
g=len(q)
del q[g-1]
print(*q,sep='')
 