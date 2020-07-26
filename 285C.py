m=int(input())
n=m
r=map(int,input().split())
f=list(r)
#print(f)
f.sort()
q=f[::-1]
#print(q)
l=len(q)
i=0
count=0
while i<l:
    y=q[i]
    if y>n:
        w=y-n
        count=count+w
    elif y<n:
        w=n-y
        count=count+w
    n=n-1        
    i+=1
print(count)