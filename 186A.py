a=input()
b=input()
l=len(a)
k=len(b)
i=0
h1=0
h2=0
f=[]
cnt=0
a1=list(a)
b1=list(b)
if l==k:
    while i<l:
        y=a[i]
        z=b[i]
        if y!=z:
            cnt+=1
            f.append(i)
        else:
            pass
        if cnt>2:
            break
        i+=1
else:
    pass

if cnt==2:    
    h1=f[0]
    h2=f[1]
    b1=list(b)
    b1[h2],b1[h1]=b1[h1],b1[h2]
    #b1[h1]=b1[h2]

    tui="".join(b1)
    #print(tui)
    if l==k:
        if cnt==2:
            if a==tui:
                print("YES")
            elif a!=tui:
                print("NO")
    elif l!=k:
        print("NO")
else:
    print("NO")
 