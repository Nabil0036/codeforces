q=int(input())
j=0
inp=[]
u=[]
while j<q:
    k=input().split(' ')
    inp.append(k)
    j+=1
#print(inp)
 
l=len(inp)
#print(l)
res=[]
i=0
d1=0
r1=0
d2=0
r2=0
tf=0
while i<l:
    p=inp[i]
    a=int(p[0])
    b=int(p[1])
    df=abs(a-b)
    if df>5:
        d1=int(df/5)
        r1=df%5
        #print('d1',d1)
        #print('r1',r1)
        if r1>=2:
            d2=int(r1/2)
            r2=r1%2
            #print('d2',d2)
            #print('r2',r2)
        elif df%5==0:
            d2=0
            r2=0
        else:
            d2=0
            r2=1    
        tf=d1+d2+r2
    elif df==4 or df==3:
        tf=2
    elif df==2 or df==1 or df==5:
        tf=1
    elif df==0:
        tf=0
    res.append(tf)
    #print(p)
    i+=1
#print(res)
g=0
while g<l:
    print(res[g])
    g+=1