a =input().split(" ")
q=int(a[0])
p=int(a[1])
i=0
j=0
n=0
m=0
jh=0
kh=0
c=input().split(" ")
k=input().split(" ")
while i<q:
    z=int(c[i])
    z1=z%2
    if z1==1:
        n+=1
    else:
        pass
    i+=1
while j<p:
    x=int(k[j])
    x1=x%2
    if x1==1:
        m+=1
    else:
        pass
    j+=1
odd1=n
even1=q-n
odd2=m
even2=p-m
##print("odd1",odd1)
##print("even1",even1)
##print("odd2",odd2)
##print("even2",even2)
if odd1<even2:
    jh=odd1
elif odd1>even2:
    jh=even2
elif odd1==even2:
    jh=odd1
if even1<odd2:
    kh=even1
elif even1>odd2:
    kh=odd2
elif even1==odd2:
    kh=even1
print(jh+kh)    