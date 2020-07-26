n=int(input())
j=n+1
f=[]
x=0
e=0
i=0
c=input().split()
#print(c)
while i<n:
    w=c[i]
    e=int(w)
    x=x+e
    i=i+1

k=x
if x!=j:
    while x>=j:
        x=x-j





m=0
h=0
u=[]
p=0
s=0
while s<5:
    m=x+s
    u.append(m)
    #print(u)
    h=int(u[s])
    if h>j:
        h=h-p*j
    if h==j:
        p=p+1
##    print(h)    
    s=s+1
##print(u)
##print('p',p)
print(s-p)
##print('x1',x)
 