import math
n=int(input())
f=[]
g=map(int,input().split())
f=list(g)
##print(f)
s=0
f.sort()
l=len(f)
##print(f)
f.reverse()
##print(f)
m=f[0]-f[l-1]
##print(m)
i=0
j=l-1
c=0
mx=f[0]
mn=f[l-1]
z=f.count(mx)
x=f.count(mn)
s=z*x
##fc=math.factorial(n)
##fcx=math.factorial(n-2)
root=0
if mx==mn:
    root=math.sqrt(s)
    final=int((root)*(root-1)/2)
else:
    final=s

print(m,final)    