n=int(input())
f=[]
i=0
while i<n:
    s=input()
    f.append(s)
    i+=1
#print(f)
j=0
while j<n:
    k=len(f[j])
    if k>10:
        g=k-2
        print(f[j][0],g,f[j][k-1],sep='')
    else:
        print(f[j])
    j+=1