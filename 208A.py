n=input()
k='WUB'
i=0
l=len(n)

g=n.replace('WUB',' ')
#print(g)
f=len(g)
count=0
while i<f:
    if g[i]==' ':
        count+=1
        i+=1
    else:
        break
    
#print(count)
b=g[count:f]
print(b)