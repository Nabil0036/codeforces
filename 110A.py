a=input()
#print(type(a))
c=a[0]
#print(c)
#print(type(c))
q=len(a)
f=[]
n=0
while n<q:
    e=ord(a[n])
    if e==52 or e==55:
        f.append(e)
    n=n+1
#print(f)
t=len(f)
j=str(t)
y=len(j)
l=0
i=0
while i<y:
    q=j[i]
    if q=='4' or q=='7':
        l=l+1

    i=i+1    
if l==y:
    print('YES')
else:
    print('NO')